#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
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
            if url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            return Mock(json=lambda: None)

        cls.mock_get.side_effect = lambda url: Mock(json=lambda: get_json(url))

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method returns
        repositories with a specific license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

    def test_public_repos_with_licence(self):
        """
        Test public_repos method returns repositories
        with a specific licence
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
