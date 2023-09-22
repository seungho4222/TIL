def bfs(s):
    visited = [0] * 101
    visited[start] = 1
    q = [s]
    max_number = s
    max_depth = 1
    while q:
        now = q.pop(0)
        for to in graph[now]:
            if visited[to]:
                continue
            visited[to] = visited[now] + 1

            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
            q.append(to)
    return max_number


for tc in range(1, 11):
    n, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = input_graph[i]
        t = input_graph[i + 1]
        graph[f].append(t)
    print(f'#{tc} {bfs(start)}')
