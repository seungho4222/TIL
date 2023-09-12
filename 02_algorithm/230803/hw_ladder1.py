import sys

sys.stdin = open('input.txt', 'r')


T = 10
for tc in range(1, T+1):
    case_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # 도착지에서 출발
    for goal in range(100):
        if matrix[99][goal] == 2:
            c = goal
    r = 99
    while r:
        # 오른쪽
        if c + 1 < 100 and matrix[r][c+1] == 1 and r != 99:
            # 못 갈때까지 쭉
            while True:
                if 0 <= c + 1 < 100 and matrix[r][c+1] == 1:
                    c += 1
                else:
                    break
        # 왼쪽
        elif c - 1 > 0 and matrix[r][c-1] == 1 and r != 99:
            # 못 갈때까지 쭉
            while True:
                if 0 <= c < 100 and matrix[r][c-1] == 1:
                    c -= 1
                else:
                    break
        # 위로
        if 0 <= r < 100 and matrix[r-1][c] == 1:
            r -= 1

    print(f'#{tc}', c)