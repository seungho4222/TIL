from collections import deque
from pprint import pprint


def sink(maps):  # 벽돌 떨구기
    for y in range(W):  # 각 열 별로
        for x in range(H - 2, -1, -1):  # 밑에서부터
            if maps[x][y] != 0:  # 벽돌이 있으면
                for n in range(H - 1, x, -1):  # 그 밑에
                    if maps[n][y] == 0:  # 빈 공간 있으면
                        maps[x][y], maps[n][y] = maps[n][y], maps[x][y]  # 떨군다 !!
                        break


def brick(cnt, maps):
    global min_v
    if cnt == N:  # 구슬 다 떨궜다
        tmp = 0  # 남은 벽돌
        for i in range(H):
            for j in range(W):
                if maps[i][j] != 0:
                    tmp += 1
        min_v = min(min_v, tmp)  # 출력값 갱신
        return
    for j in range(W):
        for i in range(H):
            if maps[i][j] != 0:  # 각 열별로 가장 위에 있는 벽돌
                new_m = deque()  # 새로운 맵
                for mr in range(H):
                    new_m.append([0] * W)
                    for mc in range(W):
                        new_m[mr][mc] = maps[mr][mc]
                new_v = [(i, j)]  # 깨진 벽돌 저장
                stack = deque()
                stack.append((i, j))  # 시작 스택
                while stack:
                    r, c = stack.pop()
                    for k in range(new_m[r][c]):  # 해당 값만큼 델타 추가 탐색
                        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 델타 탐색
                            nr, nc = r + dr * k, c + dc * k
                            if 0 <= nr < H and 0 <= nc < W and new_m[nr][nc] != 0 and (nr, nc) not in new_v:
                                new_v.append((nr, nc))
                                stack.append((nr, nc))
                for cr, cc in new_v:  # 깨진 벽돌 0으로 변경
                    new_m[cr][cc] = 0
                sink(new_m)  # 벽돌 떨구고
                brick(cnt + 1, new_m)  # 다음 구슬 쏘기
                break


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_v = 1e9
    brick(0, arr)
    if min_v == 1e9:  # 다 깨부수기
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {min_v}')
