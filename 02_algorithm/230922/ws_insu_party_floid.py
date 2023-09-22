from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())  # N: 집 수, M: 간선 수, X: 목표 집
    adjm = [[0] * (N+1) for _ in range(N+1)]  # 인접 행렬
    for _ in range(M):
        f, t, w = map(int, input().split())
        adjm[f][t] = w

    for r in range(1, N+1):
        for c in range(1, N+1):
            if r != c and adjm[r][c] == 0:  # 연결 안 된 간선은 큰 수 지정
                adjm[r][c] = int(1e9)

    # 플로이드 워샬 알고리즘 -> 모든 정점쌍 최단경로
    for k in range(1, N+1):
        for i in range(1, N+1):
            if k != i:
                for j in range(1, N+1):
                    if k != j and i != j:
                        adjm[i][j] = min(adjm[i][j], adjm[i][k] + adjm[k][j])

    # 목표 집 왕복 거리 중 최대값 출력
    max_v = 0
    for r in range(1, N+1):
        cost = adjm[r][X] + adjm[X][r]
        if cost < 1e9:
            max_v = max(max_v, cost)

    print(f'#{tc} {max_v}')
