import os
from time import time, sleep
from concurrent.futures import ProcessPoolExecutor, as_completed

import requests as req


def hit_api(url, payload, hits=10):
    t1 = time()
    _ = [req.get(url, json=payload) for _ in range(hits)]
    total_time = time() - t1
    print(f'Total Time for {hits} hits: {round(total_time, 3)}s, ', end='')
    print(f'Avg Hit: {round(total_time / hits, 3)}s, ', f'PID - {os.getpid()}')


def launchpad(url, payload, cycles):
    with ProcessPoolExecutor(max_workers=5) as executor:
        pool_dict = {
            executor.submit(
                hit_api,
                url,
                payload,
                cycle
            ): cycle for cycle in cycles
        }
    all_hits = []
    for _future in as_completed(pool_dict):
        all_hits.append(_future.result())
    return all_hits


if __name__ == '__main__':
    url = 'http://localhost:5000/addr/v1/addressmatcher'
    payload = {"customerID": 1, "dob": "01/05/1988", "income": 36000, "bureauScore": 600, "applicationScore": 900, "maxDelL12M": 10, "allowedFoir": 66, "existingEMI": 3600, "loanTenure": 16, "currentAddress": "301, Sri Laxmi Nilayam, VDOs Colony, 507001", "bureauAddress": "301, Sri Lakshmi Nilayam, VDOs Colony, Khammam, 507002"}

    print('\nSequential Hits')
    hit_api(url=url, payload=payload)
    hit_api(url=url, payload=payload, hits=100)
    hit_api(url=url, payload=payload, hits=1000)
    hit_api(url=url, payload=payload, hits=2000)
    hit_api(url=url, payload=payload, hits=3000)
    print('----------------\n')

    sleep(1.5)

    print('Concurrent Hits')
    cycles = [3600, 100, 1800, 180, 1600, 1000, 1400, 900, 3000, 1100]
    launchpad(url, payload, cycles)
    print('----------------\n')
