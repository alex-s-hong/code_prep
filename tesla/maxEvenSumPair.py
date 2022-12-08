"""
Given a circular array of N integers (that is, A[0] and A[N - 1] are adjacent to each other),
what's the maximum number of adjacent pairs that you can form whose sum are even? 
Note that each element can belong to at most one pair.

For example, if we have [5, 7, 9, 6, 3], then you should pair (5, 3) and (7, 9) to achieve the answer of two. 
Also, if we have [1, 1, 1, 1, 1, 1], then the answer is 3 (pair each adjacent element without wrapping around)
"""
from typing import List


def maxEvenSumPair(nums: List[int]) -> int:
    """
    start point
    
    """
    return max(numberOfEvenSum(0, nums), numberOfEvenSum(1, nums))


def numberOfEvenSum(start, nums):
    count = 0
    
    i = 0
    N = len(nums)
    while i < N:
        if not nums[(i+start)%N] + nums[(i+1+start)%N] & 1:
            count +=1
            i +=1
        i+=1
    
    return count

if __name__ == "__main__":
    assert maxEvenSumPair([5, 7, 9, 6, 3]) == 2
    assert maxEvenSumPair([1,1,1,1,1,1]) == 3