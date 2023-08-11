T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[-1]
    benefit = 0

    for i in range(N-2, -1, -1):
        # if max_v < arr[i]:
        #     max_v = arr[i]
        # else:
        #     benefit += max_v - arr[i]
        benefit += max(max_v - arr[i], 0)
        max_v = max(arr[i], max_v)

    print(f'#{tc} {benefit}')