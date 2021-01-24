#! usr/bin/env python3
"""
0/1 knapsack problem

col: current p
row: tasks[i] # warning: have 0 padding so tasks[i-1]

first consider only 1 task. loop for 0,...,p allowances
second consider 2 tasks
...

"""
from collections import defaultdict

def maximumTotalWeight(weights:list, tasks:list, p:int):
    # knapsack problem 0/1
    # skip the double the tasks, halves the p
    p = p // 2

    #dp = [[0 for _ in range(p+1)] for _ in range(len(tasks)+1)]
    dp = defaultdict(int)

    # row[i] = task[i+1] considered
    #rows, cols = len(dp), len(dp[0])
    rows, cols = len(tasks)+1, p + 1

    for i in range(1, rows):
        for j in range(1, cols):
            # j == current p
            if j < tasks[i-1]:
                dp[(i,j)] = dp[(i-1,j)]
            else:
                dp[(i,j)] = max(dp[(i-1,j)], dp[(i-1,j-tasks[i-1])]+weights[i-1])

    #return dp[-1][-1]
    return dp[(len(tasks), p)]




if __name__ == '__main__':
    w = [2,4,4,5]
    t = [2,2,3,4]
    p = 15
    print(maximumTotalWeight(w,t,p))

    w = [2,2,4,5]
    t = [2,2,3,4]
    p = 15
    print(maximumTotalWeight(w,t,p))

    w = [3,2,2]
    t = [3,2,2]
    p = 9
    print(maximumTotalWeight(w,t,p))

    w = [2]
    t = [2]
    p = 10
    print(maximumTotalWeight(w,t,p))
