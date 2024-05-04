#!/usr/bin/env python3
"""Annotate the function's parameters
   and return values with the appropriate types
"""

from typing import List, Tuple, Any


def element_length(lst: list[Any]) -> List[Tuple[Any, int]]:
    """
    Takes a list of items that support the len() function
    and returns a list of tuples,

    Args:
    lst (List[Any]): A list of elements that support the len() function.

    Returns:
      List[Tuple[Any, int]]: A list of tuples with each
      tuple containing an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
