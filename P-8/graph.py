vertices_input = input("vertex 정보를 입력하세요 (쉼표로 구분): ")
vertices = vertices_input.split(', ')

edges_input = input("edge 정보를 입력하세요 (쉼표로 구분): ")
edges = edges_input.split(', ')

adjList = {vertex: [] for vertex in vertices}

for edge in edges:
    v1, v2 = edge.split('-')
    adjList[v1].append(v2)
    adjList[v2].append(v1)

adjList = [adjList[vertex] for vertex in vertices]

print("\nvertex =", vertices)
print("adjList =", adjList)

def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)

from queue import Queue
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s] :
            if visited[v]==False :
                Q.put(v)
                visited[v] = True

n = len(vertices)
adjMatrix = [[0] * n for _ in range(n)]

for i, v1 in enumerate(vertices):
    for v2 in adjList[i]:
        j = vertices.index(v2)
        adjMatrix[i][j] = 1
        adjMatrix[j][i] = 1


def create_adjacent_index_list(vertices, edges):
    vertex_to_index = {vertex: idx for idx, vertex in enumerate(vertices)}

    aList = [[] for _ in range(len(vertices))]

    for edge in edges:
        v1, v2 = edge.split('-')
        idx1 = vertex_to_index[v1]
        idx2 = vertex_to_index[v2]
        aList[idx1].append(idx2)
        aList[idx2].append(idx1)

    return aList

aList = create_adjacent_index_list(vertices, edges)

print("\nA부터 시작하는 깊이우선탐색")
print("DFS:", end=' ')
visited = [False] * n
DFS(vertices, adjMatrix, 0, visited)  # 'A'부터 시작
print("\n\nA부터 시작하는 너비우선탐색")
print('BFS: ', end="")
BFS_AL(vertices, aList, 0)


def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups

from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

colorGroup = find_connected_component(vertices, adjMatrix)
print("\n\n연결성분 개수 = %d " % len(colorGroup))
print(colorGroup)

def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True
    for v in range(len(vtx)) :
        if adj[s][v] != 0 :
            if visited[v]==False:
                print("(", vtx[s], "-", vtx[v], ")", end=' ')
                ST_DFS(vtx, adj, v, visited)

print('\n깊이우선탐색을 이용한 신장트리(A vertex 기준)\n ', end="")
ST_DFS(vertices, adjMatrix, 0, [False]*len(adjMatrix))