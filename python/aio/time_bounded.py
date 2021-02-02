import sys
import asyncio as aio
from time import time_ns
from random import choice

from uvloop import EventLoopPolicy


async def stopper(uloop, termination: int=3) -> None:
    await aio.sleep(termination)
    uloop.stop()


async def waiter(concurrent_tasks: int) -> None:
    S = aio.Semaphore(concurrent_tasks)
    menu = [
        (5, 'Pasta'),
        (3, 'Salad'),
        (8, 'Briyani'),
        (7, 'Pulav'),
        (1, 'Soup'),
    ]
    all_tasks = []
    for _i in range(10):
        item = choice(menu)
        all_tasks.append(
            aio.create_task(cook(item[1], item[0], S), name=f'{_i}-{item[1]}')
        )
    for task in all_tasks:
        await task
        print(f'Name: {task.get_name()}, Result: {task.result()}')


async def cook(item: str, cook_time: int, sem) -> str:
    async with sem:
        t = time_ns()
        print(f'Started {item}')
        await aio.sleep(cook_time)
        return f'Finished {item} in {time_ns() - t}ns'


if __name__ == '__main__':
    aio.set_event_loop_policy(EventLoopPolicy())
    nio = aio.get_event_loop()
    nio.create_task(stopper(nio, 8))
    nio.create_task(waiter(5))
    nio.run_forever()
