#!/usr/bin/env python3
"""Use necessary modules"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension
    four time in parallel.

    Returns:
      float: Total runtime of the concurrent executions.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {runtime:.2f} seconds")
