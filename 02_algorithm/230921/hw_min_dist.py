from heapq import heappop, heappush


def dijkstra():
    pq = []
    heappush(pq, (0, 0))
    D[0] = 0

    while pq:
        w, v = heappop(pq)
        if D[v] < w:
            continue
        for u, uw in graph[v]:
            cost = w + uw
            if D[u] > cost:
                D[u] = cost
                heappush(pq, (cost, u))
    return D[-1]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])
    D = [1e9] * (N + 1)

    print(f'#{tc} {dijkstra()}')
