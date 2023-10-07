#!/usr/bin/env python3
"""
Multiplies a float with a float from another function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    Args: multiplier (float)
    """
    return lambda x: x * multiplier
