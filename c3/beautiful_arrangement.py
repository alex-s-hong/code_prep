from collections import defaultdict


def countArrangement(n: int) -> int:
        count = 0
        visited = defaultdict(int)
        
        def backtrack(index):
            if index > n:
                nonlocal count
                count +=1
                return
            
            for i in range(1, n+1):
                if visited[i] == 0 and (index % i == 0 or i % index == 0):
                    visited[i] = 1
                    backtrack(index+1)
                    visited[i] = 0
        
        backtrack(1)
        
        return count

assert countArrangement(1) == 1
assert countArrangement(2) == 2
assert countArrangement(6) == 36 