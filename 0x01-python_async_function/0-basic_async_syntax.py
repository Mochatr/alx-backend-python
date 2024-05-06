#!/usr/bin/env python3
""" Use the necessary modules """

import asyncio
import random
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits
    for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
      max_delays (int): Maximum delay time in seconds.

    Returns:
      float: The actual delay for which the coroutine paused.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
