#!/usr/bin/env python3
""" Use necessary modules """

import asyncio
import typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns n tasks using
    task_wait_random.

    Args:
      n (int): Number of tasks to be spawned.
      max_delay (int): Maximum delay that each task_wait_random can use.

    Returns:
      List[float]: A list of float values representing the delays.
    """
    delays_list: List[float] = []

    for _ in range(n):
        delay: asyncio.Task = task_wait_random(max_delay)
        delay_result: float = await delay

        delays_list.append(delay_result)

    return sorted(delays_list)
