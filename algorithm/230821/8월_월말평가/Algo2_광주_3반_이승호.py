T = int(input())
for tc in range(1, T+1):
    # N: 카드 수, M: 김싸피가 가져갈 순서
    N, M = map(int,input().split())
    # N장의 카드 배열
    cards = list(input().split())
    # 홀수덱, 선입선출
    B_fifo = [0] * N
    front = rear = -1
    # 짝수덱, 후입선출
    C_filo = [0] * N
    top = -1
    # 보너스 카드
    bonus = 0
    # 덱 나누기
    for card in cards:
        # 숫자면 보너스 더한 숫자를 기준으로 홀수 및 짝수 나누기
        if card != '+':
            num = int(card)
            if (num + bonus) % 2 == 0:
                top += 1
                C_filo[top] = num+bonus
            else:
                rear += 1
                B_fifo[rear] = num+bonus
        # '+' 면 보너스 1 증가
        else:
            bonus += 1
    # 김싸피가 B덱에서 가져갈 순서 및 카드
    for i in range(M):
        front += 1
    B_choice = B_fifo[front]
    # 김싸피가 C덱에서 가져갈 순서 및 카드
    for i in range(M):
        top -= 1
    # 후입선출은 카드를 뺀 후 top이 줄어듬 => 따라서 M이 세번째인견우 top은 두번만 뺌
    if top > -2:    # +1을 하면 0 이상인 경우
        C_choice = C_filo[top+1]
    # 카드가 없으면 0
    else:
        C_choice = 0

    print(f'#{tc}', B_choice + C_choice)

