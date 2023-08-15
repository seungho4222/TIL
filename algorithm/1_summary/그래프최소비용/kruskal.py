def mst_kruskal(G):
    mst = []        # 공집합
    N = len(G)
    for i in range(N):
        Make_set(i)

    G.sort(key=lambda t:t[2])       # 가중치 기준으로 정렬

    mst_cost = 0        # MST 가중치

    while len(mst) < N-1:
        u, v, val = G.pop(0)        # 최소 가중치 간선 가져오기
        if Find_set(u) != Find_set(v):
            Union(u,v)
            mst.append((u,v))       # 트리에 u, v 추가하기
            mst_cost += val


N = '정점의개수'
parents = [0] * (N+1)     # 각 정점의 부모 원소(초기설정: 자기자신)
def Make_set(x):
    # 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    parents[x] = x
# parents = [i for i in range(N+1)]

def Find_set(x):
    # x를 포함하는 집합을 찾는 오퍼레이션
    # 특정 노드에서 루트까지의 경로에 존재하는 노드가 루트를 부모로 가리키도록 갱신
    while x != parents[x]:
        x = parents[x]
    return x

def Union(x,y):
    # x와 y를 포함하는 두 집합을 통합하는 오퍼레이션
    parents[Find_set(y)] = Find_set(x)
