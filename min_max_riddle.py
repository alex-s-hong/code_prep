#!/usr/bin/env python3
"""
Given an integer array of size n, find the maximum of the minimum of every window size in the array.
"""

class Solution:

    def riddle(self, arr):
        # complete this function
        n = len(arr)

        #1 arrays for nearest smallest element on both sides
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]

        stack = []

        # left
        for i in range(n):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:   left[i] = stack[-1]
            stack.append(i)

        # right
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack: right[i] = stack[-1]
            stack.append(i)

        #2 arr[i] is a minimum of a window of length "right[i]- left[i] -1"
        # winSize of i is selected from i-th position or previous max
        # ans[i] contains the maximum of minimum of elements in window size of i
        ans = [0 for _ in range(n+1)] # because 0 is not used
        for i in range(n):
            # arr[i] is possible answer for length "right[i] - left[i] -1"
            winSize = right[i] - left[i] -1
            ans[winSize] = max(ans[winSize], arr[i])
        
        #3 fill up the empty ones with bigger window's maximum
        for i in range(n-1, 0, -1):
            ans[i] = max(ans[i], ans[i+1])

        return ans[1:]



if __name__ == "__main__":
    s = Solution()
    arr = [1, 2, 3, 5, 1, 13, 3]
    ans = s.riddle(arr)
    print(*ans)
    '''
    t = int(input())
    
    for i in range(t):
        numL = input() 
        prices = list(map(int, input().split()))
        spans = s.stock_span(prices)
        print(*spans)
    '''