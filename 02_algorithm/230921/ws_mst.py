def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 마지막 노드번호, E: 간선 수
    p = list(range(V+1))  # 0번부터 이므로 정점 수는 V+1
    edge = []
    for _ in range(E):
        s, e, w = map(int, input().split())  # 시작정점, 끝정점, 가중치
        edge.append([w, s, e])  # 정렬을 위해 가중치부터 담기
    edge.sort()

    cnt = 0  # MST 간선 수
    sum_weight = 0  # 가중치 합
    for w, s, e in edge:  # 가중치 낮은 간선부터 확인 시작
        if find_set(s) != find_set(e):  # 사이클이 없다면
            union(s, e)  # 연결 시키기
            cnt += 1
            sum_weight += w
            if cnt == V+1:  # MST 구성 완료
                break
    print(f'#{tc} {sum_weight}')
