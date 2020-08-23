#! usr/bin/env/python3
import collections

class Solution:

    def criticalConnections2(self, n, connections):
        #this works
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        for v in connections:
            graph[v[0]-1].append(v[1]-1)
            graph[v[1]-1].append(v[0]-1)
            
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
        
        #cur = 0
        #start = 0
        res = []
        self.cur = 0
       
        def dfs(node,parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur+=1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n,node)
                    
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l
                
        dfs(0,None)
        
        for u, v in connections:
            #if low[v[0]]>dfn[v[1]] or low[v[1]]>dfn[v[0]]:
            if low[u-1] > dfn[v-1] or low[v-1] > dfn[u-1]:
                #res.append(v)
                res.append([u,v])
        return res



    def criticalConnections(self, n: int, connections: list) -> list:
        #create adj hashmap
        adj = collections.defaultdict(list)
        
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(v)
    
        
        
        # dfn: order of DFS traversal
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]

        """
        cur = 0
        start = 0
        res = []
        self.cur = 0
       
        def dfs(node,parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur+=1
                for n in adj[node]:
                    if dfn[n] is None:
                        dfs(n,node)
                    
                if parent is not None:
                    l = min([low[i] for i in adj[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in adj[node]+[low[node]])
                low[node] = l
                
        dfs(0,None)

    
        """
        def dfs(node, parent, level):
            # already visited
            if dfn[node] is not None:
                return 
            
            print("Node:", node)
            
            dfn[node] = low[node] = level
            
            print ("low inside: ",low)
            print ("dfn inside: ",dfn)
            
            for nei in adj[node]:
                if not dfn[nei]:
                    dfs(nei, node, level + 1)
            
            # minimal level in the neignbors, exclude the parent
            cur = min([level] + [low[nei] for nei in adj[node] if nei != parent])    
            print ("node and cur:", node, cur)
            low[node] = cur
        
        dfs(0, None, 0)
        
        

        print ("low: ",low)
        print ("dfn: ",dfn)
        
        res = []
        for u, v in connections:
            if low[u] > dfn[v] or low[v] > dfn[u]:
                res.append([u,v])
        
        return res

if __name__ == "__main__":
    s = Solution()
    n = 4
    edges =[[0,1],[1,2],[2,0],[1,3]]

    #n = 5
    #edges =[[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]

    #amazon input (starting from 1)
    n = 9
    edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]

    n = 6
    edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

    res = s.criticalConnections2(n, edges)
    print(res)