def product(idx, total):
    global min_cost
    if total > min_cost:
        return
    if idx == N:
        min_cost = min(min_cost, total)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            product(idx + 1, total + arr[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N: 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1e9  # 총 생산 비용
    visited = [0] * N  # 방문 기록
    product(0, 0)
    print(f'#{tc} {min_cost}')
