from collections import deque


def bfs():
    global cnt
    visited = [False] * 1000001
    visited[N] = True
    q = [N]
    while True:
        save = deque()  # q 원소 계산결과 저장
        for i in q:
            if i == M:  # M 만들었다 !!
                return cnt
            if i + 1 <= 1000000 and not visited[i + 1]:
                save.append(i + 1)
                visited[i + 1] = True
            if i - 1 and not visited[i - 1]:
                save.append(i - 1)
                visited[i - 1] = True
            if i * 2 <= 1000000 and not visited[i * 2]:
                save.append(i * 2)
                visited[i * 2] = True
            if i - 10 and not visited[i - 10]:
                save.append(i - 10)
                visited[i - 10] = True
        q = save  # q 변경
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N을 M으로 만들기
    # 연산 +1, -1, *2, -10
    cnt = 0  # 연산 횟수

    print(f'#{tc} {bfs()}')
