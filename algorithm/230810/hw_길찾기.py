# import sys
#
# sys.stdin = open('input.txt', 'r')


T = 10
for tc in range(1, T + 1):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    matrix = [0] * 100
    for i in range(N):
        v1, v2 = arr[i*2], arr[i*2+1]
        matrix[v1] = v2
    print(matrix)
    