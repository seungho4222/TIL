T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0     # 최솟값의 인덱스
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    ans = max_idx - min_idx
    if max_idx < min_idx:
        ans = min_idx - max_idx

    print(f'#{tc}', ans)

'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3 
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10

'''
