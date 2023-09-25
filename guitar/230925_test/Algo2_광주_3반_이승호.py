def shoot(idx, total):  # 함수 정의
    global max_v  # 전역변수 변경
    if idx == N:  # 모든 행 사격 완료 시
        max_v = max(max_v, total)  # 출력값 비교
        return
    for i in range(N):  # 각 행마다
        if visitied[i] == 0:  # 방문하지 않은 열은
            visitied[i] = 1  # 방문체크 후
            shoot(idx+1, total + arr[idx][i])  # 다음 행 방문
            visitied[i] = 0  # 방문체크 해제 -> 동일 행, 다른 열 확인


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0  # 출력값: 최대점수
    visitied = [0] * N  # 각 열의 방문 기록
    shoot(0,0)  # 함수 실행
    print(f'#{tc} {max_v}')
