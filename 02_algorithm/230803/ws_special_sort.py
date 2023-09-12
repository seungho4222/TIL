T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            if i % 2 == 0:
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
            else:
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
    print(f'#{tc}', *nums[:10])
