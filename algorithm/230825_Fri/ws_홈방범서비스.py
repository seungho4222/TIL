import sys

sys.stdin = open('input1.txt', 'r')

# 운영 비용 = K*K + (K-1)*(K-1)
# (지불비용 * 서비스지역 내 집 수) - 운영비용 => 최대값이 되는 서비스지역 내 집 수
# 영역범위(k)는 중앙r,c에서 주변r,c 차가 k이하이면 범위

T = int(input())
for tc in range(1, T + 1):
    # N: 도시의 크기, M: 지불비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for r in range(N):
        for c in range(N):
            # 서비스 가능 범위만큼 확인
            for k in range(1, N+2):
                cnt = 0
                visited = [[0]*N for _ in range(N)]
                tmp = [(r, c)]
                if arr[r][c] == 1:
                    cnt += 1
                visited[r][c] = 1
                # bfs 탐색
                while tmp:
                    i, j = tmp.pop()
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N and (abs(ni - r) + abs(nj - c)) < k and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            tmp.append((ni, nj))
                            # 범위 내 집이면 체크
                            if arr[ni][nj] == 1:
                                cnt += 1
                # 이익 계산
                if cnt * M >= k * k + ((k - 1) * (k - 1)) and max_cnt < cnt:
                    max_cnt = cnt
    print(f'#{tc} {max_cnt}')
