#! usr/bin/env python3

"""
Given an array, for each element, return the length of the longest contiguous array ending at that element
such every number in that contiguous array is strictly less than the current element

input = [1,2,3,3]
output = [1,2,3,1]

input = [7,3,4,6,9,1,5,6,3,7,4,8,2,10]
output = [1,1,2,3,5,1,2,3,1,5,1,7,1,14]

"""

def solver(nums):
    res = []
    stack = []

    for i, elem in enumerate(nums):
        while stack and stack[-1][1] < elem:
            stack.pop()
        if not stack:
            res.append(i+1)
        else:
            res.append(i- stack[-1][0])
        stack.append((i, elem))
    return res

if __name__ == "__main__":
    input = [7,3,4,6,9,1,5,6,3,7,4,8,2,10]
    assert solver(input) == [1,1,2,3,5,1,2,3,1,5,1,7,1,14]