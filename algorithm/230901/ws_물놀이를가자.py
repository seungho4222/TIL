from collections import deque

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 가로, 세로
    arr = [list(input()) for _ in range(N)]  # W: 물, L: 땅
    memo = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                visited = [[0] * M for _ in range(N)]
                stack = deque()
                stack.append((i, j))
                cnt = 1
                while stack:
                    l = len(stack)
                    for _ in range(l):
                        r, c = stack.popleft()
                        visited[r][c] = 1
                        for dr, dc in dir:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                                stack.append((nr, nc))
                                if memo[nr][nc] == 0:
                                    memo[nr][nc] = cnt
                                else:
                                    if memo[nr][nc] != 0 and memo[nr][nc] <= memo[r][c]:
                                        stack.pop()
                                        continue
                                    memo[nr][nc] = min(memo[nr][nc], cnt)
                    cnt += 1
    result = 0
    for k in memo:
        result += sum(k)
    print(f'#{tc} {result}')