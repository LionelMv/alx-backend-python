#!/usr/bin/env python3
"""
Takes two args and returns a tuple with the second element squared.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes two parameters, returns a tuple with second element squared.
    Args:
        k (str)
        v (int or float)
    Returns: Tuple -> (k, v ** 2)
    """
    return (k, v ** 2)
