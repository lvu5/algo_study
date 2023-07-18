graph = []
dp = []
next_node = []
n = 0

def get_path(start, end):
    path = []
    global graph, dp, next_node, n

    if dp[start][end] == float('inf'):
        return path
    
    at = start
    while at != end:
        if at == -1:
            return None
        path.append(at)
        at = next_node[at][end]
        
    if next_node[at][end] == -1:
        return None
    
    path.append(end)
    return path


def solve():
    global graph, dp, next_node, n
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if dp[i][k] + dp[k][j] < dp[i][j]: # if intermediate 
                    # node 
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_node[i][j] = next_node[i][k]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-inf')
                    next_node[i][j] = -1
    return dp



def main():
    global graph, dp, next_node, n
    n = 7
    dp = [[None] * n for i in range(n)]
    next_node =  [[None] * n for i in range(n)]
    graph = [ [float('inf')] * n for i in range(n)]
    
    # graph input
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
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf'):
                next_node[i][j] = j
            dp[i][j] = graph[i][j]

    dist = solve()
    
    print(dp)
    for i in range(n):
        for j in range(n):
            path = get_path(i,j)
            if path == None:
                string = "infinity"
            elif len(path) == 0:
                string = "does not exist path from {} to {}".format(i, j)
            else:
                string = "->".join(str(p) for p in path)
            string = "is: [" + string + "]"
            print("Shortest path for {} to {} is".format(i, j), string)
            
main()
