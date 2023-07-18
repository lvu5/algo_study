"""
Things to notice:
First init the dist to infinity for every nodes except first note
dist[start] = 0


"""
matrix = []
V = len(matrix)
solved = False
dist = []
prev = []
n = 9

def get_path():

    global solved
    global dist
    global matrix
    
    if not solved:
        bellman_ford(matrix)
    return dist


def rescontruct_path(start, end):
    global n
    global prev
    global solved
    global dist
    
    path = []

    if not solved:
        bellman_ford(matrix)

    if dist[end] == float('inf'):
        return path
    
    at = end

    while prev[at] is not None:
        if prev[at] == -1 :
            return None
        path.append(at)
        at = prev[at]
        
    path.append(start)
    return path



def bellman_ford(matrix):
    global solved
    global dist
    global prev
    if solved:
        return
    
    m = len(matrix)
    n = len(matrix[0])
    
    dist = [float('inf')] * n
    
    dist[0] = 0
    prev = [None] * n
    
    for k in range(n - 1):
        for i in range(0, m):
            for j in range(0, n):
                if dist[i] + matrix[i][j] < dist[j]:
                    dist[j] = matrix[i][j] + dist[i]
                    prev[j] = i
                    
    for k in range(n - 1):
        for i in range(0, m):
            for j in range(0, n):
                if dist[i] + matrix[i][j] < dist[j]:
                    dist[j] = float('-inf')
                    prev[j] = -1

    solved = True
    
def main():
    global n
    global matrix
    global dist
    global prev
    
    n = 9

    matrix = [ [float('inf')] * n for i in range(n)]
    
    for i in range(n):
        matrix[i][i] = 0
    matrix[0][1] = 1
    matrix[1][2] = 1
    matrix[2][4] = 1
    matrix[4][3] = -3
    matrix[3][2] = 1
    matrix[1][5] = 4
    matrix[1][6] = 4
    matrix[5][6] = 5
    matrix[6][7] = 4
    matrix[5][7] = 3

    d = get_path()


    for i in range(0, n):
        # from 0 to i
        path = rescontruct_path(0, i)
        if path is None:
            print("infinity and beyond")
        else:
            strpath = "->".join(str(p) for p in path)
            print(path)
            print(strpath)
    
    
main()