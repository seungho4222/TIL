T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N: 손님수, M 초마다 K 개 생산
    arr = list(map(int, input().split()))  # N명이 각각 도착하는 시간
    arr.sort()  # 도착시간 순으로 정렬
    result = 'Possible'
    for i in range(N):
        # 누적 손님수보다 arr[i]까지의 생산량이 적으면 공급 불가
        if i+1 > arr[i]//M*K:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')