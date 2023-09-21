from collections import deque

d = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = deque()
    tmp = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.' and [i, j] not in visited:
                q = deque()
                q.append([i, j])
                while q:
                    save = deque()
                    check = True
                    for _ in range(len(q)):
                        r, c = q.popleft()
                        visited.append([r, c])
                        mine = 0
                        for dr, dc in d:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < N and [nr, nc] not in visited:
                                save.append([nr, nc])
                                if arr[nr][nc] == '*':
                                    mine += 1
                        if mine:
                            check = False
                        if check:
                            q = save


'''
델타 방향 모두 0이면 bfs 탐색 시작
연쇄 파핑 이후 남은 '.' 개수 카운트
'''
