def where_is_exit(x, y):
    q = [(x, y)]
    while q:
        r, c = q.pop()
        # 출구 찾음
        if maze[r][c] == 3:
            return 1
        # 출구 아니면 방문 체크
        maze[r][c] = 1
        # 델타 탐색
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            # 탐색 성공 좌표 큐에 넣기
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1:
                q += [(nr, nc)]
    return 0


T = 10
for tc in range(1, T + 1):
    # 입력 무시
    _ = int(input())
    # 미로 배열
    maze = [list(map(int, input())) for _ in range(16)]

    print(f'#{tc} {where_is_exit(1, 1)}')
