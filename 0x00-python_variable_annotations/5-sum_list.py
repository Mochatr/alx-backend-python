#!/usr/bin/env python3
"""Define sum_list function"""

from typing import List


def sum_list(float_list: List[float]) -> float:
    """
    Returns the sum of a list of float.

    Args:
      input_list (list[float]): list of float numbers

    Returns:
      float: the sum of a list of float.
    """
    return float(sum(float_list))
