#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    def test_org(self, org_name, expected):
        """Test that GithubOrgClient.org returns the correct value"""
        with patch('client.get_json', return_value=expected) as mock_get_json:
            client = GithubOrgClient(org_name)
            result = client.org
            self.assertEqual(result, expected)
            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url returns the correct URL"""
        payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
