def node_serch(x):
    global result
    if x == G:
        result = 1
        return
    for i in adj_m[x]:
        if not visited[i]:
            visited[i] = 1
            node_serch(i)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 연결 노드
    adj_m = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj_m[s].append(e)
    # 시작 및 도착 노드
    S, G = map(int, input().split())
    # 방문 기록
    visited = [0] * (V + 1)
    visited[S] = 1
    # 경로 있으면 1, 없으면 0
    result = 0
    node_serch(S)
    print(f'#{tc}', result)


'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
