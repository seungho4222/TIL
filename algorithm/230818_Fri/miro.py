dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    # 탈출하는데 걸린 거리(최소)
    distance = 0
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.pop(0)
            if maze[r][c] == 99:
                print(f'탈출: {distance}')
                q = []
                break
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
        distance += 1
    return distance


n = 7

maze = [[0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 99, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0]]

print(bfs(0, 0))
