# recursive 방식
def fibo1(n):
    global cnt
    cnt += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo1(n - 1) + fibo1(n - 2)
        return memo[n]


N = 30
memo = [0] * (N + 1)
memo[1] = 1
cnt = 0
print(fibo1(30), cnt)

print('======================================================================')


# iterative 방식
def fibo2(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fibo2(100))
