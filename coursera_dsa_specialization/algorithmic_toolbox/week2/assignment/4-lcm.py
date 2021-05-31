# Uses python3
import sys
import math


def prime_factors(n):
    factors = []
    while n%2 == 0:
        n = n//2
        factors.append(2)
    max_factor = int(math.sqrt(n))+1
    for i in range(3, max_factor, 2):
        while n%i == 0:
            n = n//i
            factors.append(i)
    if n > 2:
        factors.append(n)
    return factors


def lcm_naive(a, b):
    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    a, b = max([a, b]), min([a, b])
    lcm = 1
    for f in set(a_factors+b_factors):
        a_count = a_factors.count(f)
        b_count = b_factors.count(f)
        max_count = max([a_count, b_count])
        lcm *= f**max_count
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

