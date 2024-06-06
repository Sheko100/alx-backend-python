#!/usr/bin/env python3
"""Module that defines function element_length with type annotations
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """creates a list of tuples contains the length of list memebers"""
    return [(i, len(i)) for i in lst]
