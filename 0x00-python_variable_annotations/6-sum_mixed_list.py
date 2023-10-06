#!/usr/bin/env python3
"""
Takes a list of integers and floats and returns their sum.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Takes a list of floats and ints, returns their sum as a float.
    Arg: mxd_lst (list)
    Return: sum of the list elements.
    """
    return sum(mxd_lst)
