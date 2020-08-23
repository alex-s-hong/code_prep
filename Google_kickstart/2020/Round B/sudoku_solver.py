"""
Time Complexity: O(9^(m * n)) -> O(9!^m)
Space Complexity: O(m*n)
"""
from collections import defaultdict

class Solution:
    
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # store the numbers in dictionaries for validity check
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    v = int(board[row][col])
                    rows[row].add(v)
                    cols[col].add(v)
                    boxes[(row//3)*3 + (col//3)].add(v)
        
        def isValid(row, col, value):
            return value not in rows[row] and value not in cols[col] and value not in boxes[(row//3)*3 + (col//3)]
        
        def backtrack(row=0, col=0):
            # check if it reached to the end
            if row == n-1 and col == n:
                return True
            # if current row is whole-examined, change to the next
            elif col == n:
                row +=1
                col = 0
                
            if board[row][col] != ".":
                return backtrack(row, col+1)
            
            # main part
            box_id = (row//3)*3 + col//3
            
            for num in range(1, 10):
                # check whether the num can be filled
                if isValid(row, col, num):
                    # try out
                    board[row][col] = str(num)
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_id].add(num)
                    
                    # go ahead
                    if backtrack(row, col+1):
                        return True
                    
                    #turns out it is not answer... backtrack
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_id].remove(num)
            
            return False
        
        backtrack()