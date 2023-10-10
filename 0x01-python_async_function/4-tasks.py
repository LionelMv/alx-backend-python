#!/usr/bin/env python3
"""
This module returns a list of delays in ascending order.
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns 'n' tasks of 'task_wait_random'
    with the specified 'max_delay'.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay in seconds for each task.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
