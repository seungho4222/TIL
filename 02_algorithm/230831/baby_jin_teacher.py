def is_run(p):
    return p[0] == p[1] - 1 and p[1] == p[2] - 1


def is_triplet(p):
    return p[0] == p[1] == p[2]


def perm(idx, selected, n, deck, player):
    global winner
    # run 이나 triplet 확인하고 승자 결정
    if idx == 3:
        p = [deck[i] for i in selected]
        if is_run(p) or is_triplet(p):
            winner = player
        return
    # 카드를 고를 수 있는 경우의 수 n
    for i in range(n):
        if i not in selected:
            selected.append(i)
            perm(idx + 1, selected, n, deck, player)
            selected.pop()


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))  # 카드 정보
    turn = 0
    A = []
    B = []
    winner = -1

    while turn < 6:
        A.append(cards[turn * 2])
        B.append(cards[turn * 2 + 1])
        if turn >= 2:
            perm(0, [], len(A), A, 1)
            if winner != -1:
                break

            perm(0, [], len(B), B, 2)
            if winner != -1:
                break
        turn += 1

    if winner == -1:
        winner = 0
    print(f'#{tc} {winner}')
