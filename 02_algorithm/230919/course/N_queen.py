T = int(input())


# row: 현재 행 번호
# remain: 놓아야 할 퀸의 남은 개수
def backtracking(row, remain):
    global cnt
    # 1. 종료 조건
    if row == N and remain == 0:
        cnt += 1
        return

    # 2. 재귀 호출
    for i in range(N):
        can_place = True

        # 세로에 퀸이 있는지 검사
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break

        # 대각선에 퀸이 있는지 검사
        for j in range(1, row + 1):
            # 좌상
            if row - j >= 0 and i - j >= 0 and board[row - j][i - j] == 1:
                can_place = False
                break

            # 우상
            if row - j >= 0 and i + j < N and board[row - j][i + j] == 1:
                can_place = False
                break

        if can_place:
            board[row][i] = 1
            backtracking(row + 1, remain - 1)
            board[row][i] = 0


for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    board = [[0]*N for _ in range(N)]
    backtracking(0,N)

    print(f'#{tc} {cnt}')