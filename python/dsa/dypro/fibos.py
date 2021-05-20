from timeit import timeit
from functools import cache


def fib_recur(n):
    if n == 0: return 0
    elif n in [1, 2]: return 1
    else: return fib_recur(n-1) + fib_recur(n-2)


def fib_loop(n):

    if n == 0: return 0
    elif n == 1: return 1

    n0, n1 = 0, 1
    for _i in range(1, n):
        n0, n1 = n1, n0 + n1

    return n1


def fib_cache(n, cache=None):
    if n == 0: return 0
    elif n ==1: return 1

    if cache is None: cache: dict = {}
    if n in cache: return cache[n]

    res = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    cache[n] = res
    return res


@cache
def fib_lcache(n):
    if n == 0: return 0
    elif n in [1, 2]: return 1
    else: return fib_lcache(n-1) + fib_lcache(n-2)


if __name__ == '__main__':
    num = 16
    rounds = 1000000
    print('')
    print(f'Fibonacci of {num} using recursive is {fib_recur(num)}')
    print(f'Fibonacci of {num} using Loop is {fib_loop(num)}')
    print(f'Fibonacci of {num} using cache is {fib_cache(num)}')
    print(f'Fibonacci of {num} using L_cache is {fib_lcache(num)}')
    t2 = timeit('fib_loop(100)', number=rounds, globals=globals())
    t3 = timeit('fib_cache(100)', number=rounds, globals=globals())
    t4 = timeit('fib_lcache(100)', number=rounds, globals=globals())
    print('Loop Tests', float(t2))
    print('Cache Tests', float(t3))
    print('LCache Tests', float(t4))
    print('')
