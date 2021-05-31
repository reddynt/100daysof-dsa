#Uses python3

import sys

def max_num_string(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number(a):
    #write your code here
    answer = ''
    while a:
        max_digit = '0'
        for nstr in a:
            if max_num_string(nstr, max_digit):
                max_digit = nstr
        answer += max_digit
        a.remove(max_digit)
    return answer

largest_number(['2', '21'])
largest_number(['9', '4', '6', '1', '9'])
largest_number(['23', '39', '92', '0', '1'])
largest_number(['0', '0', '1', '999'])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
