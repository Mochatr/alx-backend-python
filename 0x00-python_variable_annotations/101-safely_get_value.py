#!/usr/bin/env python3
"""Define safely_get_value function"""

from typing import TypeVar, Dict, Optional


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Return the value associated with the key in the dictionary
    or the default value.

    Args:
      dct (Dict[K, V]): Dictionary
      key (K): the key in the dictionary
      default (Optional[V]): The default value to return
      if the key is not found.

    Returns:
      the value associated with the key in the dictionary
      or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
