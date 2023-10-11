#!/usr/bin/env python3
"""Yields a random float value between 0 and 10."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields random numbers
        after a 1-second delay in each iteration.

    Yields:
        float: A random float value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
