# dp + 비트마스크
def work(idx, visited):
    if dp[idx][visited]:  # 기록 있으면 반환
        return dp[idx][visited]

    if visited == v_all:  # 방문 완료
        return 1

    max_p = 0
    for j in range(N):
        if visited & (1 << j) == 0:  # 미방문 시
            total = (arr[idx][j] / 100) * work(idx+1, visited | (1 << j))  # 역으로 계산 시작
            max_p = max(max_p, total)  # 최댓값 갱신

    dp[idx][visited] = max_p  # dp 저장

    return max_p  # 맥스값 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N: 직원 수, 일 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N+1)]
    v_all = (1 << N) - 1  # 방문 완료: N이 3이면 111이 방문 완료한 것
    print(f'#{tc} {work(0, 0) * 100:.6f}')
