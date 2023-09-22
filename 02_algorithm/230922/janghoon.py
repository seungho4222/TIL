def recur(level, acc_height):
    global ans
    if acc_height >= B:
        ans = min(ans, acc_height)
        return
    if level == N:
        return
    recur(level + 1, acc_height + arr[level])
    recur(level + 1, acc_height)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    recur(0, 0)
    print(f'#{tc} {ans-B}')
