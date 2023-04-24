#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<list>

using namespace std;

void add_edge(vector<pair<int, int>> graph[], int u, int v, int wt) {
    graph[u].push_back(make_pair(v, wt));
    graph[v].push_back(make_pair(u, wt));
}

int min_distance(vector<bool> &visited, vector<int> &dist) {
    int n = dist.size();
    int min_index = -1;
    int min_val = INT_MAX;
    for(int i = 0; i < n; i++){
        if (!visited[i] && dist[i] < min_val){
            min_val = dist[i];
            min_index = i;
        }
    }
    return min_index;
}

void dijkstra_naive(vector<pair<int, int>> graph[],int src, int n) {
    vector<bool> visited(n);
    vector<int> dist(n, INT_MAX);
    dist[src] = 0;

    for(int i = 0; i < n - 1; i++) {
        int u = min_distance(visited, dist);
        visited[u] = true;
        for (vector<pair<int, int>>::iterator i = graph[u].begin(); i != graph[u].end(); i++) {
            int v = i->first;
            int wt = i->second;
            if (dist[v] < dist[u] + wt)
                dist[v] = dist[u] + wt;
        }
    }
}

void dijkstra_withQueue(vector<pair<int, int>> graph[], int src, int n){
    vector<bool> visited(n, false);
    vector<int> dist(n, INT_MAX);
    dist[src] = 0;
    // first param is the enclosed data type for the container
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int, int>>> fringe;

    fringe.push(make_pair(0, src));

    while (!fringe.empty()){
        pair<int, int> u = fringe.top();
        // first is the distance, second is node
        fringe.pop();
        for(auto i : graph[u.second]){
            int wt = i.first;
            int v = i.second;
            if (dist[v] > dist[u.second] + wt){
                dist[v] = dist[u.second] + wt;
                fringe.push(make_pair(dist[v], v));
            }
        }
    }
}

int main() {
    int n = 9;
    vector<pair<int, int>> graph[n];
}