#!/usr/bin/env python3
""" Use necessary modules """
import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio. Task that runs the wait_random
    coroutine with the specified max_delay.

    Args:
      max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
      asyncio.Task: The created task
    """
    return asyncio.create_task(wait_random(max_delay))
