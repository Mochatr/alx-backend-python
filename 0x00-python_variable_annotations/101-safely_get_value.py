#!/usr/bin/env python3
"""Define safely_get_value function"""

from typing import Mapping, Any, TypeVar, Union, Optional


T = TypeVar('T')
ret_t = Union[Any, T]
def_t = Optional[T]


def safely_get_value(dct: Mapping, key: Any,
                     default: def_t = None) -> ret_t:
    """
    Retrieve a value from a dictionary
    by key with a fallback to a default value.

    Args:
    dct : The dictionary from which to retrieve the value.
    key : The key to look up in the dictionary.
    default : The default value to return if the key is not found.

    Returns:
      The value associated with the key in the dictionary,
      or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
