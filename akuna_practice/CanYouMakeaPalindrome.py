#!/usr/bin/env python3

import time
from collections import deque

class Solution:

    #after reordering the substring any way I like, determine whether the string can be changed into a palindrome in the given number of substitution

    # as we can reorder as we want, just count the number of occurance


    def canMakePaliQueries(self, s, queries):
        N = 26
        a = ord('a')
        dp = [[0] * N]
        #import pdb; pdb.set_trace()
        for i in range(1, len(s)+1):
            new = dp[i-1]
            # clipping into 0 - 26
            j = ord(s[i-1]) - a
            new[j] += 1
            dp.append(new)
        ans = []
        for l, r, k in queries:
            L = dp[l]
            R = dp[r+1]
            ans.append(sum((R[i] - L[i]) & 1 for i in range(N)) // 2 <= k)
        return ans




if __name__ == "__main__":
    start_time = time.time()
    s = Solution()
    print(s.canMakePaliQueries(5, 10, [1,2,3,4,5,6]))
    print(s.canMakePaliQueries(5, 2, [5,1,6,2,7,3]))
    print("--- %.8f seconds ---" % (time.time() - start_time))

