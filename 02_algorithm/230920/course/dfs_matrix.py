# 인접행렬 (adjacency matrix)
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


# dfs - stack
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        if now in visited:
            continue

        visited.append(now)

        # for next in range(5):
        for next in range(4, -1, -1):
            if graph[now][next] == 0:
                continue

            if next in visited:
                continue

            stack.append(next)
    return visited


print(f'dfs stack : ', end='')
print(*dfs_stack(0))

# dfs - 재귀
visited = [0] * 5
path = []


def dfs(now):
    visited[now] = 1
    print(now, end=' ')

    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue

        dfs(next)


print(f'dfs recursive : ', end='')
dfs(0)
