import sys

sys.stdin = open('in.txt', 'r')


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우(델타)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    diff_sum = 0
    for r in range(N):
        for c in range(N):
            now_diff_sum = 0
            for d in range(4):  # 상하좌우 탐색
                nr = r + dr[d]  # 다음행 번호 = 현재 행 번호 + 이동방향에 따른 변화량
                nc = c + dc[d]  # 다음열 번호 = 현재 열 번호 + 이동방향에 따른 변화량
                # if 0 <= nr < N and 0 <= nc < N:  # 인덱스 검사
                if is_valid(nr, nc):
                    diff = arr[r][c] - arr[nr][nc]
                    diff = -diff if diff < 0 else diff
                    now_diff_sum += diff
                    # now_diff_sum += abs(arr[r][c] - arr[nr][nc])
            diff_sum += now_diff_sum

    print(f'#{tc}', diff_sum)
