from collections import deque


def dijkstra(x, y):
    q = deque()
    q.append([x, y])
    D[x][y] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                tmp = 0
                if arr[nr][nc] > arr[r][c]:
                    tmp += arr[nr][nc] - arr[r][c]
                if D[nr][nc] > D[r][c] + tmp + 1:
                    D[nr][nc] = D[r][c] + tmp + 1
                    q.append([nr, nc])
    return D[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[1e9] * N for _ in range(N)]
    print(f'#{tc} {dijkstra(0, 0)}')
