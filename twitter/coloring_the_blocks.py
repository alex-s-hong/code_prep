#! usr/bin/env python3

"""
leetcode 256. Paint House
two adjacent blocks cannot be in same colour
cost= [[1,2,3],[1,2,3],[3,3,1]]

"""

def minPrice(cost:list):
    if not cost:
        return 0

    dp = cost[0]
    for i in range(1, len(cost)):
        pre = dp[:]
        for j in range(len(dp)):
            dp[j] = cost[i][j] + min(pre[:j]+ pre[j+1:])
    
    return min(dp)


if __name__== "__main__":
    cost = [[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]
    print(minPrice(cost))

