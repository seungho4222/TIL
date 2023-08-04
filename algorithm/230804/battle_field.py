import sys

sys.stdin = open('input.txt', 'r')


# 명령 설정
def up():
    global r
    field[r][c] = '^'
    if 0 <= r-1 and field[r-1][c] == '.':
        field[r-1][c] = '^'
        field[r][c] = '.'
        r = r-1
def down():
    global r
    field[r][c] = 'v'
    if r+1 < H and field[r+1][c] == '.':
        field[r-1][c] = 'v'
        field[r][c] = '.'
        r = r+1
def left():
    global c
    field[r][c] = '<'
    if 0 <= c-1 and field[r][c-1] == '.':
        field[r][c-1] = '<'
        field[r][c] = '.'
        c = c-1
def right():
    global c
    field[r][c] = '>'
    if c+1 < W and field[r][c+1] == '.':
        field[r][c+1] = '>'
        field[r][c] = '.'
        c = c+1
def shoot():
    if field[r][c] == '^':
        for s in range(1, H):
            if 0 <= r-s and field[r-s][c] == '*':
                field[r-s][c] = '.'
                return
            elif 0 <= r-s and field[r-s][c] == '#':
                return
    elif field[r][c] == 'v':
        for s in range(1, H):
            if r+s < H and field[r+s][c] == '*':
                field[r+s][c] = '.'
                return
            elif r+s < H and field[r+s][c] == '#':
                return
    elif field[r][c] == '<':
        for s in range(1, W):
            if 0 <= c-s and field[r][c-s] == '*':
                field[r][c-s] = '.'
                return
            elif 0 <= c-s and field[r][c-s] == '#':
                return
    elif field[r][c] == '>':
        for s in range(1, W):
            if c+s < W and field[r][c+s] == '*':
                field[r][c+s] = '.'
                return
            elif c+s < W and field[r][c+s] == '#':
                return

T = int(input())
for tc in range(1, T+1):
    # 높이: H, 너비: W
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    move = ['^', 'v', '>', '<']
    # 탱크 시작 위치
    r, c = -1, -1
    for i in range(H):
        for j in range(W):
            if field[i][j] in move:
                r, c = i, j
    # 명령(order) 개수
    N = int(input())
    for o in input():
        if o == 'U' : up()
        elif o == 'D' : down()
        elif o == 'L' : left()
        elif o == 'R' : right()
        elif o == 'S' : shoot()

    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(field[i]))