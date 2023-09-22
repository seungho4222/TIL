def dfs(month, acc_cost):
    global ans
    if acc_cost > ans:
        return
    if month > 12:
        ans = min(ans, acc_cost)
        return
    dfs(month + 1, acc_cost + (months[month] * fee[0]))
    dfs(month + 1, acc_cost + fee[1])
    dfs(month + 3, acc_cost + fee[2])
    dfs(month + 12, acc_cost + fee[3])


T = int(input())
for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    months = [0] + list(map(int, input().split()))
    ans = int(1e9)
    dfs(1, 0)
    print(f'#{tc} {ans}')
