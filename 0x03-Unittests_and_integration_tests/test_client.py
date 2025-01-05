#!/usr/bin/env python3
"""Module for unit testing
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the githubOrgCLient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """Tests the org method
        """
        client = GithubOrgClient(org)
        url = client.ORG_URL.format(org=org)
        client.org
        mock.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Tests _public_repos_url method
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            expected_url = 'https://example.com'
            mock_org.return_value = {"repos_url": expected_url}
            client = GithubOrgClient('cool')
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests public_repos method
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_get_json.return_value = [{'name': 'a1'}, {'name': 'a2'}]
            mock_repos_url.return_value = 'https://public_repos_url.com'
            client = GithubOrgClient('cool')
            self.assertEqual(client.public_repos(license=None), ['a1', 'a2'])
            mock_get_json.assert_called_once()
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
        ])
    def test_has_license(self, test_repo, test_license_key, expected):
        """Tests has_license method normal behavior
        """
        has_license = GithubOrgClient.has_license(test_repo, test_license_key)
        self.assertEqual(has_license, expected)


@parameterized_class((
    'org_payload', 'repos_payload',
    'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """Intilaizes a patcher with a side_effect
        """
        def which_payload(*args):
            """Handles the passed url
            """
            patcher = cls.get_patcher.start()
            print(patcher)
            url = args[0]
            return_value = cls.org_payload
            if url == cls.org_payload['repos_url']:
                return_value = cls.repos_payload
            patcher.return_value.json.return_value = return_value

            return patcher.return_value

        cls.get_patcher = patch('requests.get', side_effect=which_payload)
        cls._client = GithubOrgClient('google')
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stops the patcher
        """
        patcher = cls.get_patcher
        patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos methos
        """
        client = self._client
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests repos with license
        """
        client = self._client
        repos = client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)
