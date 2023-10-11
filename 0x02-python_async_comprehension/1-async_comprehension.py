#!/usr/bin/env python3
"""Returns a list of float values collected from 'async_generator'"""
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous function that asynchronously comprehends and collects values
    from the 'async_generator' coroutine into a list.

    Returns:
        List[float]: A list of float values collected from 'async_generator'.
    """
    result = [i async for i in async_generator()]
    return result
