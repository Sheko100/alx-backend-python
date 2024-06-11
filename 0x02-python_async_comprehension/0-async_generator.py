#!/usr/bin/env python3
"""Module that defines an asynchronous generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a random number asynchronous"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
