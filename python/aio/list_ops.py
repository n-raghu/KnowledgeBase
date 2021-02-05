import sys
import asyncio as aio
from gc import collect
from time import time_ns
from random import sample, randint

from uvloop import EventLoopPolicy


def s_custom_sort(raw_list: list) -> list:
    cycles = len(raw_list)
    for idx in range(cycles):
        for locus in range(idx, cycles):
            try:
                if raw_list[idx] > raw_list[locus]:
                    _tmp = raw_list[idx]
                    raw_list[idx] = raw_list[locus]
                    raw_list[locus] = _tmp
            except IndexError:
                break
    return raw_list


async def uv_custom_sort(raw_list: list) -> list:
    cycles = len(raw_list)
    for idx in range(cycles):
        for locus in range(idx, cycles):
            try:
                if raw_list[idx] > raw_list[locus]:
                    _tmp = raw_list[idx]
                    raw_list[idx] = raw_list[locus]
                    raw_list[locus] = _tmp
            except IndexError:
                continue
    return raw_list


async def uv_sorter(all_lists: list) -> int:
    t = time_ns()
    all_tasks = []
    for list_ in all_lists:
        all_tasks.append(
            aio.create_task(uv_custom_sort(list_))
        )
    for task in all_tasks:
        await task
        print(task.result())
    return time_ns() - t


def s_sorter(all_lists: list) -> int:
    t = time_ns()
    for list_ in all_lists:
        print(s_custom_sort(list_))
    return time_ns() - t


def gen_random_list(n: int) -> list:
    floor = randint(1, 10_000)
    ceil = n + floor + 10_000
    return sample(range(floor, ceil), n)


if __name__ == '__main__':
    all_lists = []
    print('How many lists to be sorted: ', end='')
    num_of_lists = int(input())
    print('Elements per list: ', end='')
    elements_per_list = int(input())

    for _ in range(num_of_lists):
        all_lists.append(gen_random_list(elements_per_list))

    sio_time = s_sorter(all_lists)

    collect()

    aio.set_event_loop_policy(EventLoopPolicy())
    aio_time = aio.run(uv_sorter(all_lists))

    print('')
    print(f'All listed sorted. AIO is {aio_time - sio_time} ns faster than SIO')
