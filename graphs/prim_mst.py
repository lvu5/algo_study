import heapq
visited = []
mstEdges = []
graph = []
pq = []
n = 0

def add_edge_graph(a,b,c):
    graph[a].append([b, c])
    graph[b].append([a, c])
# weight, from, to
def add_edge(node):
    global n, graph, visited, pq, mstEdges
    visited[node] = True
    for e in graph[node]:
        if visited[e[0]] == False:
            heapq.heappush(pq, (e[1], node, e[0]))
    return
def prims(s = 0):
    global n, graph, visited, pq, mstEdges
    m = n - 1
    edgeCount, mstCost = 0, 0
    add_edge(s)
    while edgeCount != m and len(pq) != 0:
        w, f, t = heapq.heappop(pq)
        if visited[t] == True:
            continue
        mstCost += w
        mstEdges.append((f, t, w))
        edgeCount += 1
        add_edge(t)
    if edgeCount != m:
        return (None, None)
    return (mstCost, mstEdges)
    
def main():
    global n, graph, visited, pq, mstEdges
    n = 10
    graph = [[] for _ in range(n)]

    add_edge_graph(0, 1, 5);
    add_edge_graph(1, 2, 4);
    add_edge_graph(2, 9, 2);
    add_edge_graph(0, 4, 1);
    add_edge_graph(0, 3, 4);
    add_edge_graph(1, 3, 2);
    add_edge_graph(2, 7, 4);
    add_edge_graph(2, 8, 1);
    add_edge_graph(9, 8, 0);
    add_edge_graph(4, 5, 1);
    add_edge_graph(5, 6, 7);
    add_edge_graph(6, 8, 4);
    add_edge_graph(4, 3, 2);
    add_edge_graph(5, 3, 5);
    add_edge_graph(3, 6, 11);
    add_edge_graph(6, 7, 1);
    add_edge_graph(3, 7, 2);
    add_edge_graph(7, 8, 6);
    
    visited = [False] * n
    heapq.heapify(pq)
    res = prims()
    print("Mst cost: ", res[0])
    for node in res[1]:
        print("from {} to {}, cost: {}".format(node[0], node[1], node[2]))
    
    # weight, from, to
    # graph init
    
main()