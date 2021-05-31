# Uses python3
import sys


def get_fibonacci_sum(n):
    if n < 0:
        return 0
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


def fibonacci_partial_sum_naive(from_, to):
    if from_ == 0 and to == 0:
        return 0
    counter = 60
    if from_ < counter:
        from_sum = get_fibonacci_sum(from_-1)
    else:
        from_sum = get_fibonacci_sum((from_-1) % counter)
    if to < counter:
        to_sum = get_fibonacci_sum(to)
    else:
        to_sum = get_fibonacci_sum(to % counter)
    # print(from_sum, to_sum)
    return (10 + to_sum - from_sum) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
