T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10  # p1 카드패
    p2 = [0] * 10  # p2 카드패
    win = 0  # 출력값인 승자
    for i in range(12):
        if i % 2 == 0:  # p1 카드패 나눠주기
            p1[cards[i]] += 1
        else:  # p2 카드패 나눠주기
            p2[cards[i]] += 1

        if i > 3:  # p1이 3장받으면 그때부터 베이비진 체크
            for k in range(10):  # p1 먼저 0~9 카드 체크
                if p1[k] >= 3:  # 트리플렛 체크
                    win = 1; break  # ↓ 런 체크
                elif k < 8 and p1[k] >= 1 and p1[k+1] >= 1 and p1[k+2] >= 1:
                    win = 1; break
            for k in range(10):  # p2 0~9 카드 체크
                if p2[k] >= 3:
                    win = 2; break
                elif k < 8 and p2[k] >= 1 and p2[k+1] >= 1 and p2[k+2] >= 1:
                    win = 2; break
        if win:  # 승자 나오면 카드 그만 나눠주기
            break
    print(f'#{tc} {win}')
