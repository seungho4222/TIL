T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 신청서
    tt = [list(map(int, input().split())) for _ in range(N)]  # 시간표
    s = 0  # 작업 시작 시간
    cnt = 0  # 화물차 카운트
    while True:
        tmp = 24  # 작업 최대 종료시간
        work = 0  # 작업한 화물차
        for i in tt:
            if i[0] >= s:  # 작업 시작시간이 s보다 커야됨
                if tmp >= i[1]:  # 그 중에 종료시간이 가장 작은 값 저장
                    tmp = i[1]
                    work = i
        if work == 0:  # 작업한 화물차 없으면 종료
            break
        s = tmp  # 다음 작업 시작시간은 현재 작업 종료시간
        tt.remove(work)  # 작업한 화물차 제거
        cnt += 1

    print(f'#{tc} {cnt}')
