T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v, min_v = float('-inf'), float('inf')

    for i in range(N-M+1):
        prefix_sum = 0
        for j in arr[i:i+M]:
            prefix_sum += j

        if max_v < prefix_sum:
            max_v = prefix_sum
        if min_v > prefix_sum:
            min_v = prefix_sum

    ans = max_v - min_v

    print(f'#{tc}', ans)
