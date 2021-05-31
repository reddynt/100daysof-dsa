# Uses python3
import sys


def get_change(m):
    #write your code here
    denominations = [10, 5, 1]
    num_coins = 0
    for i in denominations:
        num_coins += m//i
        m = m % i
    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
