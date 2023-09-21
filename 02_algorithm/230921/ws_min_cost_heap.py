from heapq import heappush, heappop


def dijkstra(w, x, y):  # 연료량, 행좌표, 열좌표
    q = []  # 우선순위 큐
    heappush(q, [w, x, y])  # 출발점
    D[x][y] = 0
    while q:
        uw, r, c = heappop(q)  # 연료량, 행좌표, 열좌표
        if D[r][c] < uw:  # 누적 기록이 더 적다면 패스
            continue
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                cost = uw + 1  # 이동하려면 무조건 연료량 1 필요
                if arr[nr][nc] > arr[r][c]:
                    cost += arr[nr][nc] - arr[r][c]  # 높이 차 추가
                if D[nr][nc] > cost:  # 이동할 지역의 누적 연료량보다 적은 연료량으로 갈 수 있다면
                    D[nr][nc] = cost  # 이동할 지역의 누적 연료량 변경
                    heappush(q, [cost, nr, nc])  # 힙 추가
    return D[N - 1][N - 1]  # 도착지 누적 연료량


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[1e9] * N for _ in range(N)]  # 누적 연료량 체크
    print(f'#{tc} {dijkstra(0, 0, 0)}')
