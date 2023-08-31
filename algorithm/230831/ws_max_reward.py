def check(lst):
    return int(''.join(lst))


def swap(cnt):
    global max_v
    if dp[cnt][check(S)]:  # dp 기록 있으면 리턴
        return
    # 교환 횟수 모두 소모: 결과물 숫자로 바꾸고 반환
    if cnt == N:
        max_v = max(max_v, check(S))
        return
    # 바꿀 위치중 앞쪽 i, 뒤쪽 j
    for i in range(len(S)-1):
        for j in range(i+1, len(S)):
            S[i], S[j] = S[j], S[i]
            swap(cnt + 1)
            dp[cnt+1][check(S)] = 1  # dp 저장
            S[i], S[j] = S[j], S[i]


T = int(input())
for tc in range(1, T+1):
    S, N = input().split()
    S, N = list(S), int(N)
    max_v = 0
    dp = [[0]*1000000 for _ in range(N+1)]
    swap(0)
    print(f'#{tc} {max_v}')


'''
4
123 1
2737 1
32888 2
456789 10

'''