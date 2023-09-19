def f(idx, total):
    global exchange
    if total > exchange:
        return
    if idx + M[idx] >= N - 1:
        exchange = min(exchange, total)
        return
    for i in range(idx + 1, idx + M[idx] + 1):
        f(i, total + 1)


T = int(input())
for tc in range(1, T + 1):
    N, *M = map(int, input().split())  # N: 정류장 수, M: 정류장별 배터리 용량
    exchange = N  # 교체 횟수

    f(0, 0)
    print(f'#{tc}', exchange)
