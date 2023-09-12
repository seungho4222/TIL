import sys

sys.stdin = open('sum_input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 행의 합
    for i in range(100):
        sum_r = 0
        for j in range(100):
            sum_r += arr[i][j]
        if max_sum < sum_r:
            max_sum = sum_r
    # 열의 합
    for j in range(100):
        sum_c = 0
        for i in range(100):
            sum_c += arr[i][j]
        if max_sum < sum_c:
            max_sum = sum_c
    # 대각선의 합
    sum_d = 0
    for i in range(100):
        sum_d += arr[i][i]
    if max_sum < sum_d:
        max_sum = sum_d
    # 역대각선의 합
    sum_xd = 0
    for i in range(100):
        sum_xd += arr[i][99-i]
    if max_sum < sum_xd:
        max_sum = sum_xd

    print(f'#{tc}', max_sum)