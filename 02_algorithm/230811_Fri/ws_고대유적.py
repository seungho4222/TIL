T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            c = j
            while c < M and arr[i][c] == 1:
                cnt += 1
                c += 1
            if max_len < cnt:
                max_len = cnt
    for j in range(M):
        for i in range(N):
            cnt = 0
            r = i
            while r < N and arr[r][j] == 1:
                cnt += 1
                r += 1
            if max_len < cnt:
                max_len = cnt

    print(f'#{tc} {max_len}')