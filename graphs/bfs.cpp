#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

void add_edge(int a, int b, vector<vector<int>> &graph){
    graph[a].push_back(b);
    graph[b].push_back(a);
}

void bfs(int src, vector<vector<int>> &graph) {
    int n = graph[0].size();
    vector<int> visited(n, 0);
    queue<int> fringe;
    fringe.push(src);
    visited[src] = true;
    while (!fringe.empty()) {
        int u = fringe.front();
        fringe.pop();
        for(auto v : graph[u]) {
            if (!visited[v]){
                fringe.push(v);
                visited[v] = true;
            }
        }
    }
}

int main() {
    vector<vector<int>> graph;
}