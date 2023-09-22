def tour(r, c, direction, visited):  # 행, 열, 방향, 디저트 종류
    global result
    if direction == 3 and r == i and c == j and len(visited) > 3:  # 투어 성공
        result = max(result, len(visited))  # 출력값 갱신
        return

    if 0 <= r < N and 0 <= c < N and arr[r][c] not in visited:  # 이동가능하면
        new_v = visited + [arr[r][c]]  # 디저트 저장
        nr, nc = r + d[direction][0], c + d[direction][1]
        tour(nr, nc, direction, new_v)  # 방향 유지하며 탐색

        if direction != 3:  # 위 재귀에서 이동못했다면 방향 꺾고 탐색
            nr, nc = r + d[direction + 1][0], c + d[direction + 1][1]
            tour(nr, nc, direction + 1, new_v)


d = [[1, 1], [1, -1], [-1, -1], [-1, 1]]  # 마름모 방향 이동

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1  # 탐색 실패 -1
    for i in range(N-1):
        for j in range(1, N-1):
            tour(i, j, 0, [])
    print(f'#{tc} {result}')
