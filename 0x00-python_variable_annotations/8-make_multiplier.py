#!/usr/bin/env python3
"""Module that defines function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Makes and returns a multiplier function"""
    def multiply(num: float) -> float:
        """multiplu number by multiplier"""
        return num * multiplier

    return multiply
