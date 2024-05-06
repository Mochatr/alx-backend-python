#!/usr/bin/env python3
""" Use the necessary modules """

import asyncio
from typing import List
from wait_random import wait_random


async def wait_n(n: int max_delay: int) -> List[float]:
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
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    import sys

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    max_delay = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    asyncio.run(wait_n(n, max_delay))
