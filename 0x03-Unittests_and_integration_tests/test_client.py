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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns the correct list of repos"""
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client = GithubOrgClient("test_org")
            result = client.public_repos()
            expected = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
