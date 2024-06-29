#!/usr/bin/env python3
"""Testing the Utils class methods
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests the method access_nested_map of Utils class
    """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b", ), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing that access_nested_map returns the expected value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
