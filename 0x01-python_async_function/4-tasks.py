#!/usr/bin/env python3
""" Use necessary modules """
import asyncio
import random
import typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns n tasks
    using task_wait_random with the specified
    max_delay.

    Args:
      n (int): Number of tasks to be spawned.
      max_delay (int): Maximum delay that each task_wait_random
      can use.

    Returns:
      List[float]: A list of float values representing the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == "__main__":
    async def main():
        results = await tasks_wait_n(10, 10)
        print(results)

    asyncio.run(main())
