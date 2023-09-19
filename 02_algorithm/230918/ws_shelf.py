T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())  # N: 점원 수, B: 선반 높이
    tall = list(map(int, input().split()))  # 각 점원의 키
    result = 1e9  # 점원의 키로 만든 탑과 선반 높이 차

    for i in range(1, 1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):  # j번 비트가 0이 아니면
                tmp.append(tall[j])
        k = sum(tmp)
        if k >= B:
            result = min(result, k-B)

    print(f'#{tc} {result}')
