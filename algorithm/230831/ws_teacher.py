T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_list = [list(map(int, input().split())) for _ in range(N)]

    def key_f(item):
        return item[1]

    work_list.sort(key=key_f)  # 종료시간 기준 정렬

    cnt = 0  # 최대 화물차 이용 대수

    time = 0  # 시작 시간

    while work_list:
        next_work = work_list.pop(0)
        if next_work[0] >= time:
            cnt += 1
            time = next_work[1]

    print(f'#{tc}', cnt)
