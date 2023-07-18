n = 0
graph = []
dist = []
prev = []
solved = False

def get_shortest():
    global graph, n, dist, prev, solved
    if not solved:
        bellman_ford()
    return dist

def get_path(end):
    global graph, n, dist, prev, solved
    path = []
    if dist[end] == float('inf'):
        return path
    at = end
    while prev[at] is not None and prev[at] != -1:
        path.append(at)
        at = prev[at]
    path.append(0)  # start node
    return path
        
        


def bellman_ford():
    global graph, n, dist, prev, solved
    if solved: 
        return
    dist = [float('inf')] * n
    prev = [None] * n
    dist[0] = 0 # source is 0
    
    for k in range(n - 1):
        for i in range(0,n):
            for j in range(0,n):
                if dist[i] + graph[i][j] < dist[j]:
                    dist[j] = dist[i] + graph[i][j]
                    prev[j] = i
    
    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if dist[i] + graph[i][j] < dist[j]:
                    dist[j] = float('-inf')
                    prev[j] = -1
    solved = True


def main():
    global graph, n, dist, prev, solved
    n = 9
    graph = [[float('inf')] * n for i in range(n)]
    for i in range(n):
        graph[i][i] = 0
    # insert specs here
    
    graph[0][1] = 1
    graph[1][2] = 1
    graph[2][4] = 1
    graph[4][3] = -3
    graph[3][2] = 1
    graph[1][5] = 4
    graph[1][6] = 4
    graph[5][6] = 5
    graph[6][7] = 4
    graph[5][7] = 3
    
    d = get_shortest()
    print(d)
    
    for i in range(0, n):
        path = get_path(i)
        if path is None:
            print('inf path')
        else:
            strPath = "->".join(str(p) for p in path)
            print("path is from 0 to {}{}".format(i,":"), strPath)
    
main()