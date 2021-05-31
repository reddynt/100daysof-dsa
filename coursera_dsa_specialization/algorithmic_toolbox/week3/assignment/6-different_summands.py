# Uses python3
import sys
import math


def optimal_summands(n):
    summands = []
    #write your code here
    if n <= 2:
        return [n]
    range_end = math.floor(math.sqrt(2*n)) - 2
    summands += range(1, range_end)
    if range_end < 1:
        range_end = 1
    for i in range(range_end, n):
        if sum(summands) == n:
            break
        if sum(summands) + i <= n:
            summands.append(i)
        else:
            del summands[-1]
            cur_sum = sum(summands)
            summands.append(n-cur_sum)
            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
