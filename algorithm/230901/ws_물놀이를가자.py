from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 가로, 세로
    arr = [input() for _ in range(N)]  # W: 물, L: 땅
    visited = [[0] * M for _ in range(N)]  # 방문 기록
    water = deque()  # W 위치만 저장
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                water.append((i, j, 0))  # W 좌표, 땅과 거리 저장

    result = 0
    while water:  # W에서 거리 1 찾아서 방문기록하고 거리 1 에서 거리 2 찾아서 ...
        r, c, d = water.popleft()
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                water.append((nr, nc, d + 1))
                visited[nr][nc] = d+1
                result += d + 1
    print(f'#{tc} {result}')

'''
3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL

'''
