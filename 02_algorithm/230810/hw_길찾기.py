import sys

sys.stdin = open('input.txt', 'r')


T = 10
for tc in range(1, T + 1):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    matrix = [[] for _ in range(100)]
    for i in range(N):
        v1, v2 = arr[i*2], arr[i*2+1]
        matrix[v1].append(v2)
    visited = [0] * 100
    stack = []
    i = 0
    visited[i] = 1
    result = 0
    while True:
        for j in matrix[i]:
            if j == 99:
                result = 1
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[j] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

    print(f'#{tc} {result}')