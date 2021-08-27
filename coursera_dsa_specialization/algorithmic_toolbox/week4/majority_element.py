# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    # if left + 1 == right:
    #     return a[left]
    #write your code here
    
    mid = (right-left)//2 + left
    left_major = get_majority_element(a, left, mid)
    right_major = get_majority_element(a, mid+1, right)

    if left_major == right_major:
        return left_major
    # elif left_major == -1:

        
    left_count = sum(1 for i in range(left, right+1) if a[i]==left_major)
    right_count = sum(1 for i in range(left, right+1) if a[i]==right_major)

    return left_major if left_count > right_count else right_major
    if left_count > right_count:
        return left_major
    elif right_count > left_count:
        return right_major
    return -1


def majority_element_rec(nums, lo, hi):
    # base case; the only element in an array of size 1 is the majority
    # element.
    if lo == hi:
        return nums[lo]

    # recurse on left and right halves of this slice.
    mid = (hi-lo)//2 + lo
    left = majority_element_rec(lo, mid)
    right = majority_element_rec(mid+1, hi)

    # if the two halves agree on the majority element, return it.
    if left == right:
        return left

    # otherwise, count each element and return the "winner".
    left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
    right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

    return left if left_count > right_count else right

        


# get_majority_element([1,2,3,3,5,5,5,6], 0, 7)
# get_majority_element([2,3,9,2,2], 0, 4)
# get_majority_element([1,2,3,4], 0, 3)
# get_majority_element([1,2,3,1], 0, 3)
# get_majority_element([512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772], 0, 9)

nums = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
majority_element_rec(nums, 0, len(nums)-1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
