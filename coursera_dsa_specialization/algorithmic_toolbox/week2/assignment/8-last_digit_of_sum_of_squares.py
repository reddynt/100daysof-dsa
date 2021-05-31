# Uses python3
from sys import stdin


def fibonacc_num(n):
    if n == 0:
        return 0, 0
    elif n == 1:
        return 0, 1

    previous = 0
    current  = 1
    temp = None

    for _ in range(1, n):
        temp = current % 10
        current += previous
        current = current % 10
        previous = temp
    return previous, current

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous, current = fibonacc_num(n % 60)
    return ((previous + current) * current) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
