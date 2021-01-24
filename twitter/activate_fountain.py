#! usr/bin/env python3

"""
find the minimal number of fountains you need to activate to cover whole n
leetcode: 1326
max_range: max range that water can go with water reaches here as left bound
"""

def fountainActivation2(a:list):
    n = len(a)
    max_range = [0] * n
    for i, coverage in enumerate(a):
        l,r = max(0, i- coverage), min(n, i + coverage)
        max_range[l] = max(max_range[l], r-l)

    start = end = taps = 0

    while end < n-1:
        start, end = end, max(i + max_range[i] for i in range(start,end+1))
        taps +=1
        if start == end:
            return -1
    
    return taps

def fountainActivation(A) -> int:
    if not A: return 0
    N = len(A)
    max_right_end = list(range(N))
    for i, a in enumerate(A):
        max_right_end[max(i - a, 0)] = min(i + a, N-1)
        
    res, l, r = 0, 0, max_right_end[0]
    while True:
        res += 1
        # if r can reach to the end of the whole garden, return res
        if r >= N-1:
            return res
        new_r = max(max_right_end[l:r+1])
        if new_r == r:
            return -1
        l, r = r, new_r

if __name__ == '__main__':
    l = [0,0,0,3,0,0,2,0,0]
    #print(fountainActivation(l))
    print(fountainActivation(l))
    #print(minTaps(l))
    
    assert(fountainActivation(l) == 2)
    assert(fountainActivation([3,0,2,0,1,0]) == 2)
    assert(fountainActivation([3,0,1,0,1,0]) == 2)
    assert(fountainActivation([3,0,1,0,0,1]) == -1)
    assert(fountainActivation([2,0,2,0,1,0]) == 2)
    assert(fountainActivation([0,0,0,0,0]) == -1)
    assert(fountainActivation([1,2,1]) == 1)
    assert(fountainActivation([0,1,0]) == 1)