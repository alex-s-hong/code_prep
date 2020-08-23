#! usr/bin/env/python3

from collections import defaultdict


class Graph:

    def critical_router(self, numrouters: int, numlinks: int, links: list) -> list:

        # crete adj hashmap

        adj = defaultdict(list)

        for (u,v) in links:
            adj[u].append(v)
            adj[v].append(u)

        self.time = 0

        visited = [False] * numrouters
        # what if I change it to None?
        #disc = [float("Inf")] * numrouters
        disc = [None] *numrouters
        #low = [float("Inf")] * numrouters
        low = [None] * numrouters
        parent = [-1] * numrouters
        #critical router: articulation point(ap)
        ap = [False] * numrouters

        def APutil(u, visited, ap, parent, low, disc):
            visited[u] = True
            children  = 0

            #init discovery time and low 
            disc[u] = self.time
            low[u] = self.time
            self.time +=1
            print("INIT", disc[u], low[u])

            for v in adj[u]:

                if not visited[v]:
                    parent[v] = u
                    children +=1
                    APutil(v, visited, ap, parent, low, disc)

                    # check if the subtree of v has connection to ancestors of u
                    # if so, low[u] would be updated there, so adjust to low[v]
                    # why low[v]? not low[v] - 1?
                    print("A", u, low[u], v, low[v])
                    low[u] = min(low[u], low[v])

                    # case 1: root node with two or more children
                    if parent[u] == -1 and children > 1 :
                        print("case1")
                        ap[u] = True

                    # case 2: not root and low of one of its child is bigger than disc[u]
                    if parent[u] != -1 and low[v] >= disc[u]:
                        print("case2")
                        ap[u] = True
                
                elif v != parent[u]:
                    print("B")
                    low[u] = min(low[u], disc[v])

        
        print(adj)

        for i in range(numrouters):
            print("outside", i)
            if not visited[i]:
                APutil(i, visited, ap, parent, low, disc) 

        print(ap)
        
        res = []
        for idx, val in enumerate(ap):
            if val:
                res.append(idx)

        return res


if __name__ == "__main__":
    g = Graph()
    res = g.critical_router(4, 3, [[0,1],[1,2],[2,3]])
    #res = g.critical_router(7, 7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
    #res = g.critical_router(1, 0, [])
    print(res)