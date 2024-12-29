#!/usr/bin/env python3
"""Module for unit testing
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            expected_url = 'https://example.com'
            mock_org.return_value = {"repos_url": expected_url}
            client = GithubOrgClient('cool')
            self.assertEqual(client._public_repos_url, expected_url)
