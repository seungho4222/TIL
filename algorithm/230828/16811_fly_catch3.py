T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 한번에 잡을 수 있는 최대 파리 수
    for i in range(N):
        for j in range(N):  # 스프레이를 뿌릴 위치
            # + 방향
            s = arr[i][j]  # 스프레이를 뿌린 칸에서 처리되는 파리 수
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for k in range(1, M):  # 각 방향으로 뿌릴 위치
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
            # X 방향
            s = arr[i][j]  # 스프레이를 뿌린 칸에서 처리되는 파리 수
            for di, dj in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                for k in range(1, M):  # 각 방향으로 뿌릴 위치
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')
