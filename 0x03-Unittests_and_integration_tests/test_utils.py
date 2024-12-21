#!/usr/bin/env python3
"""Tests the utils.py functions
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests that the exception is raising if path is wrong"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """Tests get_json normal behavior
        """
        with patch('requests.get') as mock:
            res = mock.return_value
            res.json.return_value = expected
            self.assertEqual(get_json(url), expected)
            mock.assert_called()


class TestMemoize(unittest.TestCase):
    """Tests the memoize function
    """

    def test_memoize(self):
        """Tests the memoize function normal behavior
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42):
            newObj = TestClass()
            self.assertEqual(newObj.a_property, 42)
            self.assertEqual(newObj.a_property, 42)
            newObj.a_method.assert_called_once()
