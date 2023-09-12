T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    now_bus = 0
    charge = 0

    # 종점 도착할때까지
    while now_bus + K < N:
        f_bus = now_bus + K

        while f_bus > now_bus and f_bus not in nums:
            f_bus -= 1

        if f_bus == now_bus:
            charge = 0
            break

        now_bus = f_bus
        charge += 1

    print(f'#{tc}', charge)
