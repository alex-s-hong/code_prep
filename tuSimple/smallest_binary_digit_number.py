"""
We are given a decimal number N, we need to find the smallest multiple of N which is a binary digit number
"""
from collections import deque

def getMinimumMultipleOfBinaryDigit(A):
    if A == 0:
        return 0

    # bfs
    q = deque('1')

    visited_remainders = set()
    
    while q:
        t = q.popleft()
        print(t)

        rem = int(t) % A
        if rem == 0:
            return t
        
        if rem not in visited_remainders:
            visited_remainders.add(rem)
            q.append(t+'0')
            q.append(t+'1')
    
#print(getMinimumMultipleOfBinaryDigit(2))
#print(getMinimumMultipleOfBinaryDigit(17))
#print(getMinimumMultipleOfBinaryDigit(0))
#print(getMinimumMultipleOfBinaryDigit(1))
print(getMinimumMultipleOfBinaryDigit(13))




