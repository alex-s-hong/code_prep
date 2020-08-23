#!/usr/bin/env python3

# first find the number of cc (nCC)
# we need nCC -1 edges to connect them all
# (e.g. 3 CCs -> 2 edges to connect them all)
# for each CC of size m, m-1 edges needed
# usable edges = edge(CC_m) - m-1
# sum of usable edges >= nCC-1 yes else no

class Solution:

    def minOperations(self, comp_node: int, comp_edge: int, c_from: list, c_to: list)->int:
        if comp_node < comp_edge-1:
            return -1

        adj = [[] for _ in range(comp_node)]

        # len(c_from) and len(c_to) must be same as input constraint
        # adj filled
        for i in range(comp_edge):
            adj[c_from[i]].append(c_to[i])
            # indirected... put it from behind too
            adj[c_to[i]].append(c_from[i])

        # compute the number of connected component
        visited = [False for _ in range(comp_node)]
        n_cc = 0
        essential_edge = 0
        for v in range(comp_node):
            if not visited[v]:
                curr = self.DFS([], v, visited, adj)
                essential_edge += len(curr) -1
                n_cc +=1
        
        if essential_edge == comp_edge:
            return 0
        
        # residual edges = total edges - Sum(len(CC_i)-1)
        residual_edge = comp_edge - essential_edge

        if residual_edge >= n_cc -1:
            return residual_edge
        else:
            return -1

    def DFS(self, temp, v, visited, adj):
        visited[v] = True
        temp.append(v)

        for node in adj[v]:
            if not visited[node]:
                temp = self.DFS(temp, node, visited, adj)

        return temp  



if __name__=="__main__":
    
    s = Solution()
    ans = s.minOperations(4,3, [1,1,3], [2,3,2])
    print(ans)

    



