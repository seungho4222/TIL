def miro(arr):
    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j
    while True:
        if arr[r][c] == 3:
            return 1
        arr[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                stack.append((r, c))
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    print(f'#{tc}', miro(arr))

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
