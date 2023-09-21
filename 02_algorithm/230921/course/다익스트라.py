'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5

'''

from heapq import heappop, heappush


def dijkstra(s):
    q = []
    heappush(q, (0, s))
    D[s] = 0

    while q:
        w, v = heappop(q)  # w: 가중치, v: 정점 번호
        if D[v] < w:
            continue
        for u, uw in adjl[v]:
            cost = D[v] + uw
            if cost < D[u]:
                D[u] = cost
                heappush(q, (cost, u))
    return D


V, E = map(int, input().split())
adjl = [[] for _ in range(V)]

INF = 1e9
D = [INF] * V

for _ in range(E):
    s, e, w = map(int, input().split())
    adjl[s].append((e, w))

print(f'다익스트라 : {dijkstra(0)}')
