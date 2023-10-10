#!/usr/bin/env python3
"""This module returns the average execution time of the wait_n coroutine"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for running
    the 'wait_n' coroutine 'n' times with the specified 'max_delay'.

    Args:
        n (int): The number of times to run the 'wait_n' coroutine.
        max_delay (int): The maximum delay in seconds
            for each call to 'wait_n'.

    Returns:
        float: The average execution time per iteration in seconds.
    """
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    # await wait_n(n, max_delay)
    total_time = time.time() - s
    return total_time / n
