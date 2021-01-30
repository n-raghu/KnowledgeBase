import asyncio
from time import time
from random import randint


async def waiter() -> None:
    active_tasks = asyncio.Semaphore(3)
    await asyncio.gather(
        cook('Pasta', randint(1,9), active_tasks),
        cook('Salad', randint(1,9), active_tasks),
        cook('Briyani', randint(1,9), active_tasks),
        cook('Pulav', randint(1,9), active_tasks),
        cook('Cottage Cheese', randint(1,9), active_tasks),
        cook('Brownie', randint(1,9), active_tasks),
        cook('Fruit Salad', randint(1,9), active_tasks),
        cook('Nutty Affair', randint(1,9), active_tasks),
    )


async def cook(order: str, cook_time: int, concurrent_tasks) -> None:
    async with concurrent_tasks:
        print(f'Started Cooking {order}')
        await asyncio.sleep(cook_time)
        print(f'{order} completed in {cook_time}s')


if __name__ == '__main__':
    t = time()
    asyncio.run(waiter())
    print('Time for all recipies: ', time() - t)
