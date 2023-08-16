# 퀸 둘 수 있는지 체크
def check(r, c):
    # 같은 열 체크
    for i in range(r):
        if board[i][c] == 1:
            return False
    # 왼쪽 대각선 체크
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    # 오른쪽 대각선 체크
    for i, j in zip(range(r, -1, -1), range(c, N)):
        if board[i][j] == 1:
            return False
    return True


# n_queen 카운트
def queen(r):
    global cnt
    if r == N:
        cnt += 1
        return
    # r행 기준으로 c행에 퀸 둘 수 있는지 순회
    for c in range(N):
        # 퀸 둘 수 있으면 보드에 체크하고 다음 행 진행
        if check(r, c):
            board[r][c] = 1
            queen(r + 1)
            board[r][c] = 0
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = 0
    print(f'#{tc} {queen(0)}')
