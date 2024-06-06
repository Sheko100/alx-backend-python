#!/usr/bin/env python3
"""Module that defines sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """claculates the addition of the list members"""
    res: float = 0

    for n in input_list:
        res += n

    return res
