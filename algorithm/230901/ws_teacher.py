T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 가로, 세로
    dp = [list(input()) for _ in range(N)]  # W: 물, L: 땅
    limit = 2000
    ans = 0
    for r in range(N):
        for c in range(M):
            if dp[r][c] == 'W':
                dp[r][c] = 0
            else:
                up = dp[r-1][c] if r > 0 else limit
                left = dp[r][c-1] if c > 0 else limit
                dp[r][c] = min(up, left) + 1
    for r in range(N-1, -1, -1):
        for c in range(M-1, -1, -1):
            if dp[r][c] == 'W':
                dp[r][c] = 0
            else:
                down = dp[r+1][c] if r < N-1 else limit
                right = dp[r][c+1] if c < N-1 else limit
                dp[r][c] = min(dp[r][c], min(down, right) + 1)
                ans += dp[r][c]
    print(f'#{tc} {ans}')
