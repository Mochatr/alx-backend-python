#!/usr/bin/env python3
"""Define sum_list function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of a mixed list as a float.

    Args:
      mxd_list (List[Union[int, float]]): list of integers and float numbers

    Returns:
      float: Sum of all values within the list
    """
    return sum(mxd_list)
