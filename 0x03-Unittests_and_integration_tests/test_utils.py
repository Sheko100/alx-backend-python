#!/usr/bin/env python3
"""Testing the Utils class methods
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Sequence, Union


class TestAccessNestedMap(unittest.TestCase):
    """Tests the method access_nested_map of Utils class
    """

    @parameterized.expand([
        ("simple", {"a": 1}, ("a", ), 1),
        ("short path", {"a": {"b": 2}}, ("a", ), {"b": 2}),
        ("whole path", {"a": {"b": 2}}, ("a", "b", ), 2)
        ])
    def test_access_nested_map(
            self,
            name: str,
            nested_map: Dict,
            path: Sequence,
            expected: Union[int, Dict]
            ) -> None:
        """Testing that access_nested_map returns the expected value"""
        self.assertEual(access_nested_map(nested_map, path), expected)
