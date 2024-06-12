#!/usr/bin/env python3
"""Module that defines function measure_time
"""
from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in parallel and
    measures the runtime
    """
    start: float = time.time()
    await gather(async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    runtime: float = time.time() - start
    return runtime
