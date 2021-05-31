# Uses python3
import sys


def get_period_length(n, m):
    if n <= 1:
        return 0

    previous = 0
    current  = 1
    temp = None
    counter = 0

    while True:
        if counter > 2:
            if current % m == 1 and previous % m == 0:
                break
        temp = current
        current += previous
        previous = temp
        counter += 1
    return counter


def get_fibonacci_number(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    temp = None

    for _ in range(1, n):
        temp = current
        current += previous
        previous = temp
    return current


def get_fibonacci_huge_naive(n, m):
    counter = get_period_length(n, m)
    if counter:
        f_n = get_fibonacci_number(n % counter)
    else:
        return n
    return f_n % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
