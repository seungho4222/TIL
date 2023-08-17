T = int(input())
for tc in range(1, T+1):
    # N: 오븐크기, M: 피자개수
    N, M = map(int, input().split())
    # M개 피자 치즈 양
    Ci = list(map(int, input().split()))
    # 피자인덱스
    next_i = 0
    # 오븐을 큐로 만들기
    oven = [0] * 1000
    front = rear = -1
    # 처음에 오븐 크기만큼 피자 넣기
    for i in range(N):
        rear += 1
        oven[rear] = [i,Ci[i]]
        next_i += 1
    # 오븐에 남아있는 피자의 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1

    while True:
        # 피자 꺼내서 치즈 반으로 줄이기
        front += 1
        pizza = oven[front]
        pizza[1] //= 2
        # 치즈가 안녹았으면 다시 집어넣기
        if pizza[1]:
            rear += 1
            oven[rear] = pizza
        # 치즈가 다 녹았다면
        else:
            # 남은 피자가 있다면 남은 피자 집어넣기
            if next_i < M:
                rear += 1
                oven[rear] = [next_i, Ci[next_i]]
                next_i += 1
            # 남은 피자가 없다면
            else:
                # 오븐에 남은 피자 개수 줄이기
                remain -= 1
                # 오븐에 피자 없으면 마지막 피자 번호 출력
                if remain == 0:
                    last_idx = pizza[0]
                    break

    print(f'#{tc} {last_idx+1}')


'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

'''