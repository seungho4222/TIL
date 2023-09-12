# D[i][j] : i에서 j로 가는 최단 경로 가중치 합
# 최초 D[i][j]에는 간선 (i, j)의 가중치 저장, i에서 j로 간선이 없으면 INF

def AllpairsShortest(D):
    n = len(D) # 정점의 수
    for k in range(1, n+1):
        for i in range(1, n+1): # 단, i != k
            for j in range(1, n+1): # 단, j != k, j != i
                D[i][j] = min(D[i][k] + D[k][j], D[i][j])
