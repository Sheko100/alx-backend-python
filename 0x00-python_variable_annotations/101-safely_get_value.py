#!/usr/bin/env python3
"""Module that defines function safely_get_value with type annotations
"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Check is the value exists before accessing it"""
    if key in dct:
        return dct[key]
    else:
        return default
