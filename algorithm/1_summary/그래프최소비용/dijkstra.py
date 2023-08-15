def Dijkstra(G, r):     # G: 그래프, s: 시작정점
    N = len(G)
    D = ['inf'] * N     # D: 출발점에서 각 정점까지 최단 경로 가중치 합 저장
    P = [None] * N      # P: 최단 경로 트리 저장
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min_ = 'inf'
        for i in range(N):
            if not visited[i] and D[i] < min_:
                min_ = D[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in G[minIndex]:
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex