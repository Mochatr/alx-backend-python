#!/usr/bin/env python3
"""Annotate the function's parameters and 
   return values with the appropriate types
"""

from typing import List, Tuple, Iterable

def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """
    Takes an iterable of strings that support the len() function 
    and returns a list of tuples.

    Args:
    lst (Iterable[str]): An iterable of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples with each tuple containing a string
                            from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
