#!/usr/bin/env python3
"""Module that defines function elements_lenngth with type annotations
"""
from typing import List, Tuple, Iterator, Sequence


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """creates a list of tuples contains the length of list memebers"""
    return [(i, len(i)) for i in lst]
