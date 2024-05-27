#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class"""


import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_json(url):
            if url == "https://api.github.com/orgs/test_org":
                return cls.org_payload
            if url == "https://api.github.com/orgs/test_org/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method returns
        repositories with a specific license.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
