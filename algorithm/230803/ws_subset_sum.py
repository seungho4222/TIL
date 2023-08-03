T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # N과 K를 만족하는 부부집합 수
    set_A = [a for a in range(1, 13)]
    len_a = len(set_A)
    count = 0
    for i in range(1 << len_a):
        subset = [set_A[j] for j in range(len_a) if i & (1 << j)]
        len_sub = 0
        sum_sub = 0
        for k in subset:
            len_sub += 1
            sum_sub += k
        if len_sub == N and sum_sub == K:
            count += 1

    print(f'#{tc}', count)
