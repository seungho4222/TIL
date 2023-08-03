# count = 0
# def create_1(x):
#     global count
#     if x == 1:
#         return
    
#     if x % 3 == 0:
#         x //= 3
#         count += 1
#         return create_1(x)
#     elif x % 2 == 0 and (x-1) % 3 != 0:
#         x //= 2
#         count += 1
#         return create_1(x)
#     else:
#         x -= 1
#         count += 1
#         return create_1(x)

# create_1(int(input()))

# print(count)


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
