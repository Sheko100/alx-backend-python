#!/usr/bin/env python3
"""Module that defines function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """assigns the arguments to a tuble with squaring the value"""
    tup: Tuple[str, float] = (k, v*v)

    return tup
