# Uses python3
import sys
import math

def binary_search(a, x):
    if x < a[0] or x > a[-1]:
        return -1
    left, right = 0, len(a)
    # write your code here
    while left <= right:
        mid = left + math.floor((right - left)/2)
        if a[mid] > x:
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        elif a[mid] == x:
            return mid
    return -1


# binary_search([1, 5, 8, 12, 13, 15], 5)
# binary_search([1, 5, 8, 12, 13, 15], 8)
# binary_search([1, 5, 8, 12, 13, 15], 12)
# binary_search([1, 5, 8, 12, 13, 15], 1)
# binary_search([1, 5, 8, 12, 13], 1)
# binary_search([1, 5, 8, 12, 13, 15], 13)
# binary_search([1, 5, 8, 12, 13, 15], 15)
# binary_search([1, 5, 8, 12, 13, 15], 16)
# binary_search([1, 5, 8, 12, 13, 15], -5)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
