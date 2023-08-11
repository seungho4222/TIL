T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0

    m = N//2
    for i in range(N):
        ans += arr[m][i]
    u, d = m+1, m-1
    a, b = 1, N - 1
    while d > -1 and u < N:
        for i in range(a,b):
            ans += arr[d][i]
        for i in range(a,b):
            ans += arr[u][i]
        u += 1
        d -= 1
        a += 1
        b -= 1

    print(f'#{tc} {ans}')
