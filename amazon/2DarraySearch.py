#! usr/bin/env/python3

import collections


def minimumDistance(graph: list) -> int:
    """
    I was asked one grid problem which is a graph problem, 
    -1 is obstacle,1 is tree need to cut, 0 is empty place you can walk through, 
    after cut, tree can be walk through, you can start at any point and you can cut in any order, 
    return minimum distance you have to walk to cut all the tree, if you cannot do that, return -1.
    eg:
    [
    [1, 1, 1],
    [-1,-1,1],
    [1, 1, 1]
    ]
    return 6
    [
    [-1,1,-1],
    [1, 1, 1],
    [-1,1,-1]
    ]
    return 6
    """
    if not graph:
        return -1
    rows = len(graph)
    cols = len(graph[0])

def orangesRotting(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    # 1. find all rotten oranges and put them in the queue
    q = collections.deque()
    fresh_orange = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                q.append((row, col, 0))
            elif grid[row][col] == 1:
                fresh_orange +=1
                
    # 2. bfs
    res = 0
    while q:
        cr, cl, time = q.popleft()
        res = time
        for x, y in [(cr, cl+1), (cr, cl-1), (cr+1, cl), (cr-1, cl)]:
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                grid[x][y] = 2
                fresh_orange -=1
                q.append((x, y, time+1))

    return res if fresh_orange == 0 else -1
    
if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid))
