graph = []
n = 0
ordering = []

def dfs(i, at, ordering, visited):
    visited[at] = True
    for node in graph[at]:
        if visited[node] == False:
            dfs(i + 1, node, ordering, visited)
    ordering[i] = at
    return i - 1
    
    
    
    return
    
def main():
    global graph, n
    visited = [False] * n
    ordering = [0] * n
    i = n - 1
    for at in range(0, n):
        if visited[at] == False:
            i = dfs(i, at, ordering, visited)
    return ordering