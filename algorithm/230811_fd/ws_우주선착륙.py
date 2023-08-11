T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, -1, 1]

    ans = 0
    for i in range(N):
        for j in range(M):
            r, c, = i, j
            cnt = 0
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] < arr[r][c]:
                    cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')
