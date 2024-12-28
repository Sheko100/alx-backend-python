#!/usr/bin/env python3
"""Module for unit testing
"""
import unittest
from unittest.mock import patch
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
        client.org()
        mock.assert_called_once_with(url)
