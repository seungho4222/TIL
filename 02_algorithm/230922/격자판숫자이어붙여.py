def dfs(y, x, number):
    if len(number) == 7:
        result.add(number)
        return
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny < 0 or ny >= 4:
            continue
        if nx < 0 or nx >= 4:
            continue
        dfs(ny, nx, number + maps[ny][nx])


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    maps = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')
