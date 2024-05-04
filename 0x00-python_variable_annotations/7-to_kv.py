#!/usr/bin/env python3
"""Define to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> float:
    """
    Returns a tuple containing the string
    and the square of the numeric value as a float.

    Args:
      k (str): string
      v (Union[int, float]): integers and float numbers

    Returns:
      Tuple[str, float]: A tuple
    """
    return (k, float(v ** 2))
