#!/usr/bin/env python3
"""This module returns the average execution time of the wait_n coroutine"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for running the wait_n coroutine
        'n' times with the specified 'max_delay'.

    Args:
        n (int): The number of times to run the wait_n coroutine.
        max_delay (int): The maximum delay in seconds for each call to wait_n.

    Returns:
        float: The average execution time per iteration in seconds.
    """
    start_time = time.time()  # Record the start time

    # Run the wait_n coroutine 'n' times with the specified 'max_delay'
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time

    # Calculate and return the average time per coroutine execution
    return total_time / n
