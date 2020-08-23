#!/usr/bin/env python3

class SortedArrangement:
    """
    Your are given n and an input array with n numbers.
    You have to tell the minimum number of operations needed to pick each element from the input array make a sorted arrangement.
    Every insertion and removal is 1 operation.
    A sorted arrangement is basically an array that is sorted.
    lets understand with example..
    let n be 4
    and input array be 2 4 1 3
    so first we take 2 and insert in the empty sorted arrangement. so 1 operation
    then the sorted arrangement is- 2
    then we pick 4 and put it in the sorted arrangement.. so we would put after 2 so 1 operation
    then the sorted arrangement is- 2 ,4
    then we pick 1 and put it in the left so 1 operation..
    then the sorted arrangement is- 1,2,4
    (now this is important)
    now we pick 3 and put we can either remove 1 and 2 put 3 and then again put 2 and 1 back or we can remove 4 , put 3 and again put 4.
    obviously the latter takes 3 operations and former takes 5 operations. so we would perform the latter one.
    answer is 1+1+1+3=6 operations.

    constraints
    N<10^5
    """

    def minimumOperations(nums: list) -> int:
        """
        minimum operations to create the sorted list from the list of numbers in given order
        """
        total = 0
        #map = {}
        pipe = []

        for i in range(len(nums)):
            if i == 0:
                total += 1
                pipe.append(nums[i])
            
            if i == 1:
                if pipe[0] < nums[i]:
                    pipe.insert(0, nums[i])


        









