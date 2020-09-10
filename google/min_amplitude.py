#! usr/bin/env python3
"""
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements.
Amplitude is the range of the array (basically difference between largest and smallest element).

example 1
Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

example 2
Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
"""

class Min_amplitude:

    def solution1(self, arr):
        # sort the array then remove the edge element of 3
        # Space Complexity = O(1), Time Complexity = O(n log n)
        if len(arr) < 5:
            return 0
        
        arr.sort()

        # removing: 4 cases (0:3), (1,2), (2,1), (3,0)
        min_gap = arr[-4] - arr[0]
        min_gap = min(min_gap, arr[-3] - arr[1])
        min_gap = min(min_gap, arr[-2]- arr[2])
        min_gap = min(min_gap, arr[-1]- arr[3])

        return min_gap
        
    def solution2(self, arr):
        """
        use only big 4 and small 4 and find the smallest difference amongst them
        create two heap (maxheap, minheap)  
        8 * log n  
        """
        pass
    

if __name__ == "__main__":
    tests = [[-1, 3, -1, 8, 5, 4], [10, 10, 3, 4, 10]]

    m = Min_amplitude()

    for test in tests:
        print(m.solution1(test))

    