#!/usr/bin/env python3
""" Use the necessary modules """

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time per execution of wait_n
    called with n and max_delay.

    Args:
      n (int): Number of times wait_random should be spawned.
      max_delay (int): Maximum delay that wait_random can use.

    Returns:
      float: The average time per execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 10
    max_delay = 10
    average_time = measure_time(n, max_delay)
    print(f"Average execution time: {average_time:.2f} seconds")
