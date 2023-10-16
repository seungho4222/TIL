def min_operations_to_one(N):
    # memoization을 위한 배열 초기화
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        # 1을 뺀 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[N]

# 예시
N = 22
result = min_operations_to_one(N)
print(result)  # Output: 3 (10 → 9 → 3 → 1)
