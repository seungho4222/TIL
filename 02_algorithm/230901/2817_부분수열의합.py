def f(i, N, s, K, rs):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    elif s > K:
        return
    elif s + rs < K:  # 남은 수를 모두 더해도 K가 안되면 리턴
        return
    else:
        f(i + 1, N, s + arr[i], K, rs - arr[i])
        f(i + 1, N, s, K, rs - arr[i])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    # for i in range(1 << N):
    #     s = 0
    #     for j in range(N):
    #         if i & (1 << j):
    #             s += arr[j]
    #     if s == K:
    #         cnt += 1
    f(0, N, 0, K, sum(arr))
    print(f'#{tc} {cnt}')

''' 
1
20 55
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

'''
