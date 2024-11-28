INF = 9999

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end='')
            else:
                print(f"{A[i][j]:4d} ", end='')
        print("")

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = [list(row) for row in adj]
    visit = [[-1] * vsize for _ in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    visit[i][j] = k

    return A, visit

def generate_path(visit, i, j, path):
    if visit[i][j] == -1:
        return
    k = visit[i][j]
    generate_path(visit, i, k, path)
    path.append(k)
    generate_path(visit, k, j, path)

def print_path_floyd(vertex, dist, visit, start, end):
    vsize = len(vertex)
    start_idx = vertex.index(start)
    end_idx = vertex.index(end)

    path = [start_idx]
    generate_path(visit, start_idx, end_idx, path)
    path.append(end_idx)

    path_str = " -> ".join(vertex[idx] for idx in path)
    distance = dist[start_idx][end_idx]

    print(f"* Shortest Path: {path_str}")
    print(f"* Distance of the Shortest Path: {distance}")

if __name__ == "__main__":
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0,     7,     INF,   INF,   3,     10,    INF],
        [7,     0,     4,     10,    2,     6,     INF],
        [INF,   4,     0,     2,     INF,   INF,   INF],
        [INF,   10,    2,     0,     11,    9,     4],
        [3,     2,     INF,   11,    0,     13,    5],
        [10,    6,     INF,   9,     13,    0,     INF],
        [INF,   INF,   INF,   4,     5,     INF,   0]
    ]

    print("Shortest Path By Floyd's Algorithm")
    dist, visit = shortest_path_floyd(vertex, weight)

    start = input("Start Vertex: ").strip()
    end = input("End Vertex: ").strip()

    print_path_floyd(vertex, dist, visit, start, end)
