import sys

sys.stdin = open('in.txt', 'r')


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_pang = 0
    for r in range(N):
        for c in range(M):
            pang = arr[r][c]
            for d in range(4):
                for k in range(1, arr[r][c] + 1):
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k
                    if is_valid(nr, nc):
                        pang += arr[nr][nc]
            if max_pang < pang:
                max_pang = pang
    print(f'#{tc}', max_pang)
