T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 양세는 시작 숫자
    # 중복 제거 숫자 저장
    tmp = set()
    # 카운트 증가할때 마다 양 숫자 ->
    sheep = 0
    while True:
        sheep = sheep + N
        # 양세는 숫자 저장
        for i in str(sheep):
            tmp.add(i)
        # 0~9까지 다 봤으면 브레이크
        if len(tmp) == 10:
            break
    print(f'#{tc}', sheep)
