T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # A, B에 속한 정수 개수
    A = sorted(list(map(int, input().split())))  # 정렬된 리스트가 조건
    B = list(map(int, input().split()))
    cnt = 0  # B의 원소가 A에 속하는지?
    for num in B:
        l = 0
        r = N - 1
        check = 0
        while l <= r:
            m = (l + r) // 2
            if A[m] == num:
                cnt += 1
                break
            elif num < A[m] and check != 'left':  # 같은 구간 연속탐색 X
                check = 'left'
                r = m - 1
            elif num > A[m] and check != 'right':  # 같은 구간 연속탐색 X
                check = 'right'
                l = m + 1
            else:  # 같은 구간 연속탐색이면 브레이크
                break

    print(f'#{tc} {cnt}')
