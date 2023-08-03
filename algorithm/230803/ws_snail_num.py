def snail_num(r, c, num, way):
    if num == N*N+1:
        return
    if 0 <= r < N and 0 <= c < N and matrix[r][c] == 0:
        matrix[r][c] = num
        nr = r + dr[way % 4]
        nc = c + dc[way % 4]
        snail_num(nr, nc, num + 1, way)
        if num != 17:
            nr = r + dr[(way + 1) % 4]
            nc = c + dc[(way + 1) % 4]
            snail_num(nr, nc, num + 1, way + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snail_num(0, 0, 1, 0)
    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])
