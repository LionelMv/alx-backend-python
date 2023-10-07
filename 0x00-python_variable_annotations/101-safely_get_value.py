#!/usr/bin/env python3
"""
Understanding of TypeVar.
Returns a value in a dictionary if it exists.
Otherwise defaults to None.
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Returns a value if exists in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
