# 너비우선탐색
def bfs(S):
    # 이동칸 카운트
    visited = [0] * (V + 1)
    q = [S]
    visited[S] = 1
    while q:
        t = q.pop(0)
        # 도착 시 출발카운트 1 빼고 출력
        if t == G:
            return visited[t] - 1
        # 이동가능하면 큐 쌓고 이동칸 +1 체크
        for w in adj_l[t]:
            if not visited[w]:
                q += [w]
                visited[w] = visited[t] + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V + 1)]
    # 인접 리스트 생성
    for i in range(E):
        # 간선의 양쪽 노드 번호
        v1, v2 = map(int, input().split())
        adj_l[v1] += [v2]
        adj_l[v2] += [v1]
    # S: 출발노드, G: 도착노드
    S, G = map(int, input().split())

    print(f'#{tc}', bfs(S))

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
1 5
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
