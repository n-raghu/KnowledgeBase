import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

from parsers.tgm_banknifty import stream


stream(1)
