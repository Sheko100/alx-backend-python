#!/usr/bin/env python3
"""Module defines task_wait_n function
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random function n times"""
    wait_list: List[float] = []

    for i in range(n):
        wait = await task_wait_random(max_delay)
        wait_list.append(wait)

    return sorted(wait_list.copy())
