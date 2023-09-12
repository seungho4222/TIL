def move(r, c, total):  # 행, 열, 합계
    global min_v
    if r == N-1 and c == N-1:  # 오른쪽 아래 도착시 값 비교
        min_v = min(min_v, total)
        return
    for dr, dc in [[0,1], [1, 0]]:  # 오른쪽, 아래만 이동
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:  # 이동가능하면 이동 후 재귀
            move(nr, nc, total + arr[nr][nc])
    return min_v


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1e9
    print(f'#{tc} {move(0,0,arr[0][0])}')
