T = int(input())
for tc in range(1, T + 1):
    # D:기차 거리, A: 속력, B: 속력, C: 파리속력
    D, A, B, F = map(int, input().split())
    dist = 0

    while D > 10 ** (-7):
        dist += D / (B + F) * F
        D -= D / (B + F) * (A + B)
        dist += D / (A + F) * F
        D -= D / (A + F) * (A + B)
    print(f'#{tc} {dist:.10f}')

'''
1
250 10 15 20

'''
