#!/usr/bin/env python3
"""Module that defines function safe_first_element with type annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[..., None]:
    """Checks if the argument is defined before accessing it"""
    if lst:
        return lst[0]
    else:
        return None
