#!/usr/bin/env python3
"""Module to define an asynchronous function
"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Waits for a random time between 0 to max_delay"""

    rndm: float = random.uniform(0, max_delay)

    await asyncio.sleep(rndm)

    return rndm
