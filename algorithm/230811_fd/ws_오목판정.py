def concave(arr):
    for i in range(N):
        for j in range(N-4):
            cnt = 0
            c = j
            while c < N and arr[i][c] == 'o':
                cnt += 1
                c += 1
            if cnt >= 5:
                return 'YES'

    for j in range(N):
        for i in range(N-4):
            cnt = 0
            r = i
            while r < N and arr[r][j] == 'o':
                cnt += 1
                r += 1
            if cnt >= 5:
                return 'YES'

    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            r = i
            c = j
            while r < N and c < N and arr[r][c] == 'o':
                cnt += 1
                r += 1
                c += 1
            if cnt >= 5:
                return 'YES'

    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            r = i
            c = N-1-j
            while r < N and 0 <= c and arr[r][c] == 'o':
                cnt += 1
                r += 1
                c -= 1
            if cnt >= 5:
                return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {concave(arr)}')
