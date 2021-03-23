import os
import sys
from time import time, sleep
from math import ceil as mceil
from datetime import datetime as dtm
from concurrent.futures import ProcessPoolExecutor, as_completed

from rarfile import RarFile


def gen_list_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def unlocker(rarfile, pwd_chunk, tracker, start):
    tx_ = time()
    with RarFile(rarfile, 'r') as rfile:
        one_file = rfile.namelist()[0]
        for i,p in enumerate(pwd_chunk):
            if i % 1000 == 0:
                _t = time()
                txt = f'{i}, cycle_time: {round(_t - tx_, 1)}, time_until_start: {round(_t - start, 1)}, PID: {os.getpid()}'
                with open(tracker, 'a') as trk_file:
                    trk_file.write(txt)
                    trk_file.write('\n')
                tx_ = time()
            try:
                with rfile.open(one_file, pwd=p.strip()) as f:
                    f.read()
                print(p)
                with open(f'{rarfile}.pwd', 'a') as gfile:
                    gfile.write(p)
                return p
            except Exception:
                continue
    return False


def aio_unlocker(
    rar_file: str,
    tracker: str,
    passwords: list,
    start_stamp,
):
    parts_per_5 = len(passwords) / 5
    if parts_per_5 > 10_000:
        processes = 5
    else:
        processes = 3
    processes = 5 if parts_per_5 > 10_000 else 3
    chunks = gen_list_chunks(passwords, mceil(len(passwords) / processes))

    with open(tracker, 'a') as tfile:
        tfile.write(f'Testing with {len(passwords)} using {processes} concurrent processes\n\n\n')

    with ProcessPoolExecutor(max_workers=processes) as executor:
        ppool = {
            executor.submit(
                unlocker,
                rar_file,
                chunk,
                tracker,
                start_stamp
            ): chunk for chunk in chunks
        }

    for future in as_completed(ppool):
        res = future.result()
        if res:
            with open(f'{rar_file}.pwd', 'w') as pfile:
                pfile.write(str(res))
            executor.shutdown(wait=False)


if __name__ == '__main__':
    start_epoch = time()
    rar_file = 'goa.rar'
    passwords_file = 'goa_openers_1.txt'
    tracker_file = 'goa_report.trk'

    with open(tracker_file, 'w') as tfile:
        tfile.write(f'Unlocking RAR started at {dtm.fromtimestamp(start_epoch)}\n')

    with open(passwords_file, 'r') as pfile:
        all_passwords = pfile.readlines()

    aio_unlocker(
        rar_file=rar_file,
        tracker=tracker_file,
        passwords=all_passwords,
        start_stamp=start_epoch,
    )

    with open(tracker_file, 'a') as tfile:
        tfile.write(f'\n\nCompleted in {round(time() - start_epoch, 1)}s\n\n')
