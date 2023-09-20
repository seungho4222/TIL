# 인접행렬 (adjacency matrix)
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def bfs(start):
    visited = [0] * 5

    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for next in range(5):
            if graph[now][next] == 0:
                continue

            if visited[next]:
                continue

            queue.append(next)
            visited[next] = 1


print(f'bfs queue : ', end='')
bfs(0)
