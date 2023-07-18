graph = []
def dfs(i, at, visited, ordering):
    visited[at] = True
    for node in graph[at]:
        if visited[node] == False:
            dfs(i, at, visited, ordering)
    ordering[i] = at
    return i - 1



def main():
    n = 8
    
    visited = [False] * n
    ordering = [0] * n
    i = n - 1
    for at in range(n):
        if visited[at] == False:
            i = dfs(i, at, visited, ordering)
    return ordering