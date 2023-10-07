#!/usr/bin/env python3
"""
Takes a sequence and returns a list of tuples.
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples with lenth of each"""
    return [(i, len(i)) for i in lst]
