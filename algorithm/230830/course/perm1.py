def f(i, N):
    if i == N:  # 순열 완성
        print(p)
        return
    else:  # p[i]에 들어갈 숫자 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이라면
                p[i] = card[j]
                used[j] = 1
                f(i + 1, N)
                used[j] = 0


card = list(map(int, input()))
used = [0] * 6  # 이미 사용한 카드인지 표시
p = [0] * 6
f(0, 6)
