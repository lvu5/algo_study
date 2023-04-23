#include<iostream>
#include <algorithm>


using namespace std;

/**
The idea for union-find by rank is to keep track of the
height for each nodes, then we compare the height for each
whichever is larger will be the parent (or the representative)
for the other one.
**/
int parent[100];
int ranks[100];

int find(int v){
    if (parent[v] == v)
        return parent[v];
    else
        return parent[v] = find(parent[v]); // path compression
}

void makeset(int v){
    parent[v] = v;
    ranks[v] = 0;
}

void union_sets(int a, int b){
    a = find(a);
    b = find(b);
    if (a != b){ // meaning different parent
        // we compare the ranks
        if (ranks[a] > ranks[b])
            swap(a,b); // now a=b and b=a
            // b is now > a
        parent[b] = a;

        if (ranks[a] == ranks[b]) // pure random
            ranks[a]++;
        // either ranks[a]++ or ranks[b]++
    }
}

int main() {

} 