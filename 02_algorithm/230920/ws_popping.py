from collections import deque

d = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = deque()

    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                mine = 0
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == '*':
                            mine += 1


'''
8방향 모두 0이면 bfs 탐색 시작
연쇄 파핑 이후 남은 '.' 개수 카운트
'''
