#! /usr/bin/env python3

"""
Imagine you place a knight chess piece on a phone dial pad. 
This chess piece moves in an uppercase “L” shape: two steps horizontally 
followed by one vertically, or one step horizontally then two vertically:
Suppose you dial keys on the keypad using only hops a knight can make. 
Every time the knight lands on a key, we dial that key and make another hop. 
The starting position counts as being dialed.
How many distinct numbers can you dial in N hops from a particular starting position?
"""

import time

NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

def neighbors(position):
    return NEIGHBORS_MAP[position]

def yield_sequence(start, N, sequence=None):
    if sequence is None:
        sequence = [start]
    
    if N  == 0:
        yield sequence
        return

    for neighbor in neighbors(start):
        yield from yield_sequence(neighbor, N-1, sequence+[neighbor])

def print_sequence(start, N):
    for sequence in yield_sequence(start, N):
        print(sequence)

def count_sequence_naive(start, N):
    """
    C(S, N) = sum(C(neighbour of S, N-1))

    time complexity = (number of neighbors)^N
    """
    if N == 0:
        return 1
    
    res = 0

    for neighbor in neighbors(start):
        res += count_sequence_naive(neighbor, N-1)

    return res

def count_sequence(start, N):
    """
    dynamic programming
    """
    if start == 5:
        return 0

    prev = [1]*10 # initially, it's 1 for all numbers if N == 0 (its own number)
    curr = [0]*10

    curr_N = 1

    while curr_N <= N:        
        for position in range(10):
            for neighbor in neighbors(position):
                curr[position] += prev[neighbor]

        # prep for next
        prev = curr
        curr = [0]* 10
        curr_N +=1

    return prev[start]


if __name__ == "__main__":
    print("start, N :", end=' ')
    start, N = map(int,input().split())
    tic = time.perf_counter()
    #print(count_sequence_naive(start, N))
    print(count_sequence(start, N))
    toc = time.perf_counter()
    print(f"Execution time: {toc-tic:0.4f} seconds")