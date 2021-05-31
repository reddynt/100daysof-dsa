# Uses python3
import sys


def get_period_length(n, m):
    if n <= 1:
        return 0

    previous = 0
    current  = 1
    temp = None
    counter = 0
    part_sum = 1

    while True:
        if counter > 2:
            if current % m == 1 and previous % m == 0:
                break
        temp = current
        current += previous
        previous = temp
        counter += 1
        part_sum = part_sum % 10 + current % 10
    return counter, part_sum


def get_fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    temp = None
    sum = 1

    for _ in range(1, n):
        temp = current
        current += previous
        previous = temp
        sum = sum % 10 + current
    return sum % 10


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    counter, part_sum = get_period_length(n, 10)
    if n < counter:
        rem = get_fibonacci_sum(n)
        return rem%10
    else:
        rem = get_fibonacci_sum(n % counter)
        return rem % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
