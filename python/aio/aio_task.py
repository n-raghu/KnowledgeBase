import asyncio as aio
from time import time
from random import randint

from uvloop import EventLoopPolicy


async def waiter(concurrent_tasks) -> None:
    S = aio.Semaphore(concurrent_tasks)
    all_tasks = [
        aio.create_task(cook('Pasta', randint(1,9), sem=S), name='pasta'),
        aio.create_task(cook('Salad', randint(1,9), sem=S)),
        aio.create_task(cook('Briyani', randint(1,9), sem=S)),
        aio.create_task(cook('Pulav', randint(1,9), sem=S)),
        aio.create_task(cook('Cottage Cheese', randint(1,9), sem=S)),
        aio.create_task(cook('Brownie', randint(1,9), sem=S)),
        aio.create_task(cook('Fruit Salad', randint(1,9), sem=S)),
        aio.create_task(cook('Nutty Affair', randint(1,9), sem=S)),
    ]
    for task in all_tasks:
        await task
        print(f'Name: {task.get_name()}, Result: {task.result()}')


async def cook(order: str, cook_time: int, sem) -> None:
    async with sem:
        print(f'Started Cooking {order}')
        await aio.sleep(cook_time)
        return f'Finished {order} in {cook_time}s'


if __name__ == '__main__':
    aio.set_event_loop_policy(EventLoopPolicy())
    t = time()
    aio.run(waiter(5))
    print('Time for all recipies: ', round(time() - t, 3))
