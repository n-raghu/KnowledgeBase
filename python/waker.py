import sys
from time import sleep

try:
    sleep_time = sys.argv[1]
except Exception:
    sleep_time = 516000 # 5 days

sleep(sleep_time)
