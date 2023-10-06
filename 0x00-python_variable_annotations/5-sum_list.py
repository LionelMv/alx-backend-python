#!/usr/bin/env python3
"""
Takes a list of floats and returns their sum.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes a list of floats, returns their sum.
    Arg: input_list (float)
    Return: sum of input list elements.
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
