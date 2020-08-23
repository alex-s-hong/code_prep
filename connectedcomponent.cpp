//#include <bits/stdc++.h>
#include <iostream>
#include <list>

using namespace std;

class Graph{
    // number of vertices
    int V;
    // pointer to an array containing adjacency lists
    list<int>* adj;

    void DFSUtil (int v, bool visited[]);

public:
    // constructor
    Graph (int V);

    void addEdge(int v, int w);
    int NumberOfconnectedComponents();

};

int Graph::NumberOfconnectedComponents(){
    
    // Mark all the vertices as not visited
    bool* visited = new bool[V];
    
    int count = 0;
    for (int v=0; v < V; v++){
        if (visited[v] == false){
            DFSUtil(v, visited);
            count +=1;
        }
    }
    return count;
}

void Graph::DFSUtil (int v, bool visited[]){
    
    // mark the current node as visited
    visited[v] = true;

    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator it;

    for (it = adj[v].begin(); it != adj[v].end(); it++){
        if (!visited[*it]){
            DFSUtil(*it, visited);
        }
    }

}

Graph::Graph(int V){
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
    adj[w].push_back(v);
}

int main(){
    Graph g(5);
    g.addEdge(1, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 4);

    cout << g.NumberOfconnectedComponents()<< endl;

    return 0;
}
