#!/usr/bin/env python3
"""Module that defines sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """claculates the addition of the list members"""
    res: float = 0

    for n in mxd_lst:
        res += n

    return res
