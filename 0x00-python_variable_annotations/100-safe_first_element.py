#!/usr/bin/env python3
"""Define safe_first_element function"""

from typing import Callable


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the iterable, None otherwise.

    Args:
      lst (Sequence): Sequence of elements of any type.

    Returns:
      the first element of the iterable.
    """
    if lst:
        return lst[0]
    else:
        return None
