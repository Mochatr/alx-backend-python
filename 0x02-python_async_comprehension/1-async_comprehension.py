#!/usr/bin/env python3
"""Use necessary modules"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect and return 10 random numbers
    using an async comprehension.

    Returns:
      List[float]: A list of 10 random numbers.
    """
    return [n async for n in async_generator()]

if __name__ == "__main__":
    asyncio.run(async_comprehension())
