graph = []
dp = []
next_node = []
n = 0

def get_path(start, end):
    path = []
    at = start
    if dp[start][end] == float('inf'): # no path
        return path
    while at != end:
        if at == - 1:
            return None
        path.append(at)
        at = next_node[at][end]
    if next_node[at][end] == -1:
        return None
    path.append(end)
    return path

def solve():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_node[i][j] = next_node[i][k]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-inf')
                    next_node[i][j] = -1 # negative cycle
    return dp

def main():
    global graph, dp, next_node, n
    n = 7
    graph = [ [float('inf')] * n for i in range(n)]
    next_node = [ [None] * n for i in range(n)]
    dp = [ [float('inf')] *n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf'):
                next_node[i][j] = j # next node to go to dest (j) from i is j
            dp[i][j] = graph[i][j]
    for i in range(n):
        graph[i][i] = 0
    
    graph[0][1] = 2;
    graph[0][2] = 5;
    graph[0][6] = 10;
    graph[1][2] = 2;
    graph[1][4] = 11;
    graph[2][6] = 2;
    graph[6][5] = 11;
    graph[4][5] = 1;
    graph[5][4] = -2;
    
    
    
    
    return