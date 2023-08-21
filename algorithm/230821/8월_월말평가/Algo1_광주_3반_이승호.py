T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대값, 최소값 출력용
    max_v = 0
    min_v = 1e9
    # 배열 순회
    for r in range(N):
        for c in range(N):
            # 기준 풍선점수 포함
            total = arr[r][c]
            # 상하좌우 풍선 탐색
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                # 기준 풍선점수만큼 추가 탐색
                for k in range(1, arr[r][c] + 1):
                    nr = r + dr * k
                    nc = c + dc * k
                    # 배열 범위 내면 점수 포함
                    if 0 <= nr < N and 0 <= nc < N:
                        total += arr[nr][nc]
            # 최대값 및 최소값 비교 후 변경
            if max_v < total:
                max_v = total
            if min_v > total:
                min_v = total

    print(f'#{tc}', max_v - min_v)
