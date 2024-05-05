#!/usr/bin/env python3
"""Define safely_get_value function"""

from typing import TypeVar, Dict, Optional


K = TypeVar('K')  # Generic type for the key
V = TypeVar('V')  # Generic type for the value


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Retrieve a value from a dictionary by key with a fallback to a default value.

    Args:
    dct (Dict[K, V]): The dictionary from which to retrieve the value.
    key (K): The key to look up in the dictionary.
    default (Optional[V]): The default value to return if the key is not found.

    Returns:
    Optional[V]: The value associated with the key in the dictionary, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
