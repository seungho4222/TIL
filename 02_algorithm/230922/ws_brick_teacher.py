from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def pick(n, bricks, remain):
    global answer
    if n == N or remain == 0:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if bricks[i][j]:
                    cnt += 1
        answer = min(answer, cnt)
        return

    for c in range(W):
        now_bricks = [[bricks[i][j] for j in range(W)] for i in range(H)]
        q = deque()
        for r in range(H):
            if now_bricks[r][c]:
                q.append((r, c, now_bricks[r][c]))
                now_bricks[r][c] = 0
                break
        if not q:
            continue
        b_cnt = 0
        while q:
            i, j, k = q.popleft()
            b_cnt += 1
            for l in range(1, k):
                for d in range(4):
                    ni = i + dr[d] * l
                    nj = j + dc[d] * l
                    if 0 <= ni < H and 0 <= nj < W and now_bricks[ni][nj]:
                        if now_bricks[ni][nj] > 1:
                            q.append((ni, nj, now_bricks[ni][nj]))
                        now_bricks[ni][nj] = 0
        for j in range(W):
            for i in range(H - 1, -1, -1):
                if not now_bricks[i][j]:
                    find = False
                    for ni in range(i - 1, -1, -1):
                        if now_bricks[ni][j]:
                            find = True
                            now_bricks[i][j] = now_bricks[ni][j]
                            now_bricks[ni][j] = 0
                            break
                    if not find:
                        break
        pick(n + 1, now_bricks, remain - b_cnt)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    answer = W * H * 10

    remain = 0
    for r in range(H):
        for c in range(W):
            if bricks[r][c] != 0:
                remain += 1
    pick(0, bricks, remain)
    print(f'#{tc} {answer}')
