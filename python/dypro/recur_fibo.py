def fib(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(f'Fibonacci of 5 is {fib(5)}')
    print('Enter custom number to find fibonacci: ', end='')
    num = int(input())
    print(f'Fibonacci of {num} is {fib(num)}')
