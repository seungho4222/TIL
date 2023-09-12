def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:  # 1~9에 빠진 숫자 있으면
                return 0  # 0 리턴
    for j in range(9):
        cnt = [0] * 10
        for i in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                return 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 10
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    cnt[arr[r][c]] += 1
            for k in range(1, 10):
                if cnt[k] == 0:
                    return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)

    print(f'#{tc} {ans}')

'''
1
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

'''