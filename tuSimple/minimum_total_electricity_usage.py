
from collections import defaultdict, deque

def minimum_total_usage(N, M, relationships):
    # relationship... graph? if cycle -> -1
    # create graph, bfs?

    dic = defaultdict(list)
    indegree = defaultdict(int)

    for prev, after in relationships:
        dic[prev].append(after)
        indegree[prev]
        indegree[after]+=1
    
    queue = deque()

    res = N*M

    path = []

    for elem, degree in indegree.items():
        if degree == 0:
            queue.append((elem,0))
    
    weights = defaultdict(int)

    while queue:
        elem, level = queue.popleft()
        path.append(elem)

        for nextelem in dic[elem]:
            indegree[nextelem] -=1
            if indegree[nextelem]==0:
                queue.append((nextelem, level+1))
                weights[nextelem] = level+1

    #cycle
    if len(path) != len(indegree):
        return -1
    
    return res + sum(weights.values())



print(minimum_total_usage(10, 2, [[1,2],[1,3]]))
print(minimum_total_usage(10, 1, [[7,5],[6,5],[5,4],[4,1],[4,2],[5,3]]))
print(minimum_total_usage(10, 1, [[2,6],[7,5],[6,5],[5,4],[4,1],[4,8],[5,3]]))
print(minimum_total_usage(10, 1, [[4,5],[7,5],[6,5],[5,4],[4,1],[4,2],[5,3]]))
