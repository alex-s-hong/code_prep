import collections

def numSquarefulPerms(A: [int]) -> int:
        """
        1. count the number occurance
        2. for i, find j that i+j is square
        3. backtrack
        
        """
        output = 0
        count = collections.Counter(A)
        unique = list(count.keys())
        
        
        def backtrack(cur):
            if len(cur) == len(A):
                nonlocal output
                output += 1
                return
            for i in range(len(unique)):
                if len(cur) == 0:
                    cur.append(unique[i])
                    count[unique[i]] -=1
                    backtrack(cur)
                    cur.pop()
                    count[unique[i]] +=1
                    
                elif count[unique[i]] > 0 and int((cur[-1] + unique[i])**0.5)**2 == cur[-1]+unique[i]:
                    cur.append(unique[i])
                    count[unique[i]] -=1
                    backtrack(cur)
                    count[unique[i]] +=1
                    cur.pop()
        

        backtrack([])
        
        return output

print(numSquarefulPerms([2,2,2,2])) # 1
print(numSquarefulPerms([1,17,8])) #2
print(numSquarefulPerms([1,3,6]))
print(numSquarefulPerms([1,3,2]))
