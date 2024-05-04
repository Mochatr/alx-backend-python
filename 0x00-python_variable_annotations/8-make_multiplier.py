#!/usr/bin/env python3
"""Define multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its input
    by a specified multiplier.

    Args:
      multiplier (float): The factor by which
      the returned function will multiply its input.

    Returns:
      Callable[[float], float]: A function that multiplies
      a given float by the multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
