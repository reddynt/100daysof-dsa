# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    refill_pos = 0
    n_refills = 0
    previous_stop = 0
    stops.append(distance)
    for stop in stops:
        if refill_pos + tank >= stop:
            previous_stop = stop
        else:
            refill_pos = previous_stop
            n_refills += 1
            previous_stop = stop
            if refill_pos + tank < stop:
                return -1
    return n_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
