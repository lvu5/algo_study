#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void add_edge(int a, int b, vector<vector<int>> &graph) {
    graph[a].push_back(b);
    graph[b].push_back(a);
}

void dfs_helper(int u, vector<vector<int>> &graph, vector<int> visited) {
    // according to clrs
    // white = no visited yet,
    // grey = visting
    // black = ended
    visited[u] = true;
    // explored time set start here
    for(auto v : graph[u]){
        if (!visited[u])
        // if you want to get the predecessor, add them there
            dfs_helper(v, graph, visited);
    }
    // explored time end here
    // mark them black
}

void dfs(vector<vector<int>> &graph, vector<int> visited) {
    int n = graph[0].size();
    for(int i = 0; i < n; i++)
        dfs_helper(i, graph, visited);
}

int main() {
    vector<vector<int>> graph;
}