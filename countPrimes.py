class Solution:
    
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0
        
        board = [True] * n 
        
        board[0], board[1] = False, False
        
        for i in range(2, int(n**0.5) +1):
            if board[i]:
                #j = i*i # start from i*i as i*2... i*(i-1) is already dealt beforehand
                #while j < n:
                 #   board[j] = False
                  #  j +=i
                
                board[i*i:n:i] = [False] *len(board[i*i:n:i])
        
        return sum(board)