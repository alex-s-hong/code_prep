from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # topological sort: detect cycle
        # maintain children, num_of_parents dic, probe starting from nodes with no parents
        kids = {i:[] for i in range(numCourses)}
        num_parents = {i:0 for i in range(numCourses)}
        
        for cur, pre in prerequisites:
            kids[pre].append(cur)
            num_parents[cur] +=1
            
        no_parents = deque()
        for key, val in num_parents.items():
            if val == 0:
                no_parents.append(key)
        
        seen = set(no_parents)
        
        # cycle exists
        if not seen:
            return False
        
        while no_parents:
            cur = no_parents.popleft()
            
            for kid in kids[cur]:
                if kid in seen:
                    return False
                num_parents[kid] -=1
                if num_parents[kid] == 0:
                    no_parents.append(kid)
                    seen.add(kid)
        
        return len(seen) == numCourses