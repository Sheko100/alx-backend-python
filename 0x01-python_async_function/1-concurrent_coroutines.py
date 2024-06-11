#!/usr/bin/env python3
"""Module defines wait_n function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random function n times"""
    wait_list: List[float] = []
    highest: float = 0.0
    i: int = 0

    for i in range(0, n):
        wait = await wait_random(max_delay)
        wait_list.append(wait)

    i = 0
    while i < len(wait_list):
        if len(wait_list) - 1 != i and wait_list[i] > wait_list[i + 1]:
            tmp: float = wait_list[i]
            wait_list[i] = wait_list[i + 1]
            wait_list[i + 1] = tmp
        elif i - 1 >= 0 and wait_list[i - 1] > wait_list[i]:
            tmp: float = wait_list[i]
            wait_list[i] = wait_list[i - 1]
            wait_list[i - 1] = tmp

        i += 1

    return wait_list
