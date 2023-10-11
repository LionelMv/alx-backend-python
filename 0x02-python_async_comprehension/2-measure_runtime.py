#!/usr/bin/env python3
"""Returns the total runtime in s for running 'async_comprehension' 4 times."""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures the total runtime for running
    the 'async_comprehension' coroutine four times concurrently and returns
    the total runtime in seconds.

    Returns:
        float: The total runtime in seconds for running
            'async_comprehension' four times.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.time() - start_time

    return total_runtime
