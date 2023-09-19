T = int(input())
for tc in range(1, T+1):
    N, *M = map(int, input().split())  # N: 정류장 수, M: 정류장별 배터리 용량
    exchange = 0  # 교체 횟수
    start = 0  # 시작 정류장

    while start < N-1:
        move = 0
        if start + M[start] >= N - 1:  # 종점 갈 수 있는 정류장 도착
            break

        for i in range(start+1, start+M[start]+1):  # 현재 갈 수 있는 정류장
            if move <= i + M[i]:  # 다음에 최대로 갈 수 있는 정류장
                move = i + M[i]
                start = i
        exchange += 1

    print(f'#{tc} {exchange}')
