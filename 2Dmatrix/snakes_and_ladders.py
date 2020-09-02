from collections import deque
import copy

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # flatten to 1d map
        onedmap = {}
        
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                # rows == even
                if rows & 1 == 0:
                    if i & 1 == 0:
                        # go reverse
                        onedmap[cols*(rows-i-1)+(cols-j)] = board[i][j]
                    else:
                        # go forward
                         onedmap[cols*(rows-i-1)+(j+1)] = board[i][j]
                # rows == odd
                else:
                    if i & 1 == 0:
                        # go forward
                        onedmap[cols*(rows-i-1)+(j+1)] = board[i][j]
                    else:
                        # go reverse
                        onedmap[cols*(rows-i-1)+(cols-j)] = board[i][j]

        
        #print(onedmap)
        #bfs
        visited = set()
        q = deque([(1,0)])
        visited.add(1)
        d = rows * cols
        while q:
            loc, steps = q.popleft()
            #visited.add(loc)
            
            if loc == d:
                #print(process)
                return steps
                     
            for x in range(1, 7):
                
                if x + loc <= d and (x+loc) not in visited:
                    visited.add(x+loc)
                    
                    if onedmap[x+loc] != -1:
                        #newp = copy.copy(process)
                        #newp.append(onedmap[x+loc])
                        q.append((onedmap[x+loc], steps+1))
                    
                    else:
                        #newp = copy.copy(process)
                        #newp.append(x+loc)
                        q.append((x+loc, steps+1))

        return -1
