#!/usr/bin/env python3
""" Use the necessary modules """

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An Asynchronous routine that spawns wait_random n times
    with specified max_delay.

    Args:
      n (int): Number of times wait_random should be spawned.
      max_delay (int): Maximum delay that wait_random can use.

    Returns:
      List[float]: A list of float values representing the delay
      returned in ascending order of completion.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []

    for future in asyncio.as_completed(tasks):
        result = await future
        results.append(result)

    return result

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    max_delay = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    results = asyncio.run(wait_n(n, max_delay))
    print(f"Delays: {results}")
