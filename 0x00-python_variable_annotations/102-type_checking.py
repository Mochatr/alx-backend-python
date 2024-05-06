#!/usr/bin/env python3
"""Define zoom_array function"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return zoomed in list

    Args:
      lst (Iterable[T]) : An iterable of any items.
      factor (int) : The number of times to replicate
      each item (default is 2).

    Returns:
      Zoomed in list.
    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
