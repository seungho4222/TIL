T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    max_start = 0
    for p in range(N):
        for q in range(N):
            i, j = p, q
            cnt = 1
            start = arr[i][j]

            while True:
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break

            if max_cnt < cnt:
                max_cnt = cnt
                max_start = start
            elif max_cnt == cnt and max_start > start:
                max_start = start
    print(f'#{tc} {max_start} {max_cnt}')
