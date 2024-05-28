#!/usr/bin/env python3
"""Unit tests for utils.get_memoize function"""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid path"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")
        
        class TestMemoize(unittest.TestCase):
            """Test class for memoize decorator"""
            def test_memoize(self):
                """Test memoize decorator caches results properly"""
                class TestClass:
                    def a_method(self):
                        return 42

                    @memoize
                    def a_property(self):
                        return self.a_method()
                with patch.object(TestClass, 'a_method',
                                  return_value=42) as mock_method:
                    test_obj = TestClass()
                    self.assertEqual(test_obj.a_property, 42)
                    self.assertEqual(test_obj.a_property, 42)
                    mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
