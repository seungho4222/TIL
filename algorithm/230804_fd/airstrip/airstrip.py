import sys

sys.stdin = open('in.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    # 단차 표시
    matrix_r = [[0] * N for _ in range(N)]
    matrix_c = [[0] * N for _ in range(N)]
    # 활주로 중복방지
    dupl_r = [[0] * N for _ in range(N)]
    dupl_c = [[0] * N for _ in range(N)]
    road = 0
    # 행,열 반복 확인

    # 행기준 빈매트릭스에 단차 표시 1
    for i in range(N):
        for j in range(N - 1):
            if land[i][j] > land[i][j + 1]:
                matrix_r[i][j + 1] += 1
            elif land[i][j] < land[i][j + 1]:
                matrix_r[i][j] += 1
    # 좌우 X만큼 동일값 이어지면 단차표시 0으로
    for i in range(N):
        for j in range(N):
            if matrix_r[i][j] == 1 and 0 <= j - 1 and land[i][j] + 1 == land[i][j - 1]:
                cnt = 0
                for x in range(1, X):
                    if j + x < N and land[i][j] == land[i][j + x] and dupl_r[i][j+x] == 0:
                        cnt += 1
                if cnt == X - 1:
                    matrix_r[i][j] = 0
                    for xx in range(X):
                        dupl_r[i][j+xx] += 1
            elif matrix_r[i][j] == 1 and j + 1 < N and land[i][j] + 1 == land[i][j + 1]:
                cnt = 0
                for x in range(1, X):
                    if 0 <= j - x and land[i][j] == land[i][j - x] and dupl_r[i][j-x] == 0:
                        cnt += 1
                if cnt == X - 1:
                    matrix_r[i][j] = 0
                    for xx in range(X):
                        dupl_r[i][j-xx] += 1
    # 빈 매트릭스 각 행의 합이 0이면 활주로 설치
    for i in range(N):
        check = 0
        for j in range(N):
            if matrix_r[i][j]:
                check += 1
        if not check:
            road += 1

    # 열기준 빈매트릭스에 단차 표시 1
    for j in range(N):
        for i in range(N - 1):
            if land[i][j] > land[i + 1][j]:
                matrix_c[i + 1][j] += 1
            elif land[i][j] < land[i + 1][j]:
                matrix_c[i][j] += 1
    # 상하 X만큼 동일값 이어지면 단차표시 0으로
    for j in range(N):
        for i in range(N):
            if matrix_c[i][j] == 1 and 0 <= i - 1 and land[i][j] + 1 == land[i - 1][j]:
                cnt = 0
                for x in range(1, X):
                    if i + x < N and land[i][j] == land[i + x][j] and dupl_c[i+x][j] == 0:
                        cnt += 1
                if cnt == X - 1:
                    matrix_c[i][j] = 0
                    for xx in range(X):
                        dupl_c[i+xx][j] += 1
            elif matrix_c[i][j] == 1 and i + 1 < N and land[i][j] + 1 == land[i + 1][j]:
                cnt = 0
                for x in range(1, X):
                    if 0 <= i - x and land[i][j] == land[i - x][j] and dupl_c[i-x][j] == 0:
                        cnt += 1
                if cnt == X - 1:
                    matrix_c[i][j] = 0
                    for xx in range(X):
                        dupl_c[i-xx][j] += 1
    # 빈 매트릭스 각 열의 합이 0이면 활주로 설치
    for j in range(N):
        check = 0
        for i in range(N):
            if matrix_c[i][j]:
                check += 1
        if not check:
            road += 1

    print(f'#{tc}', road)