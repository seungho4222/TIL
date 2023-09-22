T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 사람 수, M: 관계 수
    graph = [[] for _ in range(N + 1)]  # 인접 리스트
    for _ in range(M):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited = [0] * (N+1)  # 방문기록
    group = 0  # 총 그룹 수
    for i in range(1, N+1):  # 각 번호 확인
        if visited[i]:  # 이미 그룹에 속했다면 패스
            continue
        stack = [i]
        while stack:  # 그룹 만들기 시작
            now = stack.pop()
            visited[now] = 1
            for next in graph[now]:
                if visited[next]:
                    continue
                stack.append(next)
        group += 1
    print(f'#{tc} {group}')
