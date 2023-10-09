#!/usr/bin/env python3
"""
An asynchronous coroutine function, wait_random.
Takes an int, returns the delay which is random.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive).

    Args:
        max_delay (float, optional): The maximum delay in seconds (inclusive).
        Default is 10 seconds.

    Returns:
        float: A random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
