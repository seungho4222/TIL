T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 출석번호(1~N), M: 신청서
    arr = list(map(int, input().split()))  # 신청서 정보 한줄로 받기
    graph = [[] for _ in range(N + 1)]  # 인접 리스트
    for i in range(M):
        graph[arr[2 * i]].append(arr[2 * i + 1])
        graph[arr[2 * i + 1]].append(arr[2 * i])
    visited = []  # 방문 기록
    group = 0  # 전체 몇개 조?
    for i in range(1, N+1):  # 출석 번호 순회
        if i in visited:  # 이미 확인한 번호면 스킵
            continue
        stack = [i]  # 스택 시작
        while stack:
            now = stack.pop()
            visited.append(now)  # 방문 저장
            for to in range(len(graph[now])):  # 연결된 정보만 확인
                next = graph[now][to]
                if next in visited:  # 이미 확인한 번호면 스킵
                    continue
                stack.append(next)  # 새 번호면 저장
        group += 1  # 연결된 하나의 그룹 찾았다 !!
    print(f'#{tc} {group}')