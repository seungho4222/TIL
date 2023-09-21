from heapq import heappop, heappush


def prim(s):
    heap = []
    MST = [0] * V
    MIN_V = 0
    heappush(heap, (0, s))

    while heap:
        w, v = heappop(heap)

        if MST[v]:
            continue
        MST[v] = 1

        MIN_V += w
        for u in range(V):
            if adjm[v][u] == 0 or MST[u]:
                continue
            heappush(heap, (adjm[v][u], u))

    return MIN_V


V, E = map(int, input().split())
adjm = [[0] * V for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adjm[s][e] = w
    adjm[e][s] = w

print(f'최소신장트리 : {prim(0)}')
