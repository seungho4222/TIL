'''
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''

V, E = map(int, input().split())

adj_lst = [[] for _ in range(V + 1)]

for i in range(E):
    s, e = map(int, input().split())

    # s에서 e로 가는 길 존재
    adj_lst[s].append(e)
    # e에서 s로 가는 길 존재
    adj_lst[e].append(s)

# 재귀를 이용해서 구현

visited = [0] * (V + 1)
visited[1] = 1


def dfs(now):
    print(now)
    # 현재 정점에서 방문할 수 있는 정점을 찾아서 방문
    for next in adj_lst[now]:
        # now에서 방문할 수 있는 next 정점
        if not visited[next]:
            visited[next] = 1
            dfs(next)  # 재귀 호출


dfs(1)
