#!/usr/bin/env python3
"""Module defines function measure_runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Executes wait_n function and measures its runtime"""
    start: float = time.time()

    asyncio.run(wait_n(n, max_delay))

    total_time: float = time.time() - start

    return total_time / n
