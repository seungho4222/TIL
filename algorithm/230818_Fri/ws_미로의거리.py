# 출발(2) 인덱스 찾기
def start_idx():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

# 너비우선탐색
def bfs(x, y):
    # 출발점에서 이동한 칸 숫자 체크
    visited = [[0] * N for _ in range(N)]
    # 출발점 1
    visited[x][y] = 1
    # 큐 쌓기
    q = [(x, y)]
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.pop(0)
            # 출구 찾으면 출력: 출발점, 도착점 값 2빼주기
            if maze[r][c] == 3:
                return visited[r][c] - 2
            # 델타 탐색
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                # 이동가능하면 큐 쌓고 1칸 이동 체크
                if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q += [(nr, nc)]
                    visited[nr][nc] = visited[r][c] + 1
    # 출구 못찾으면 0 출력
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 미로 배열
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 인덱스
    sti, stj = start_idx()
    print(f'#{tc} {bfs(sti, stj)}')


'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

'''
