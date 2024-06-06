#!/usr/bin/env python3
"""Module that defines sum_list function
"""


def sum_list(input_list: list[float]) -> float:
    """claculates the addition of the list members"""
    res: float = 0

    for n in input_list:
        res += n

    return res
