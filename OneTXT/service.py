import sys
from multiprocessing import Queue, Process

from parsers.tgm_banknifty import stream as stream_nifty
from parsers.goldflints import stream as stream_goldflints

queue = Queue(369)

Process(target=stream_goldflints, args=(queue,)).start()
Process(target=stream_nifty, args=(queue,)).start()


while True:
    print(queue.get(), flush=True)
