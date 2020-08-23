#!/usr/bin/env python3
class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for _ in range(V)] 
  
    def DFSUtil(self, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True

        for i in self.adj[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def NumberOfConnectedComponent(self):

        #construct visited list
        visited = [False for _ in range(self.V)]

        count = 0
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                count +=1
        
        return count
    
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
    

if __name__=="__main__":
    g = Graph(8)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(1, 3)
    print(g.NumberOfConnectedComponent())
  