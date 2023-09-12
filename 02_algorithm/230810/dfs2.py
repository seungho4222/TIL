dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]


def dfs(r, c, n):
    visited = [[0] * n for _ in range(n)]
    stack = []
    visited[r][c] = 1

    while True:
        if arr[r][c] == 3:
            print('도착')
            break
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                stack.append((r, c))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break