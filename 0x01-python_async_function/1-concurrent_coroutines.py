#!/usr/bin/env python3
"""Module defines wait_n function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random function n times"""
    wait_list: List[float] = []

    for i in range(n):
        wait = await wait_random(max_delay)
        wait_list.append(wait)

    return sorted(wait_list.copy())
