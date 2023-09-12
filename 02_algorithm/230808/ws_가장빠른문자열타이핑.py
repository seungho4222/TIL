T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    # A, B의 인덱스
    ai = 0
    bi = 0

    cnt = 0
    while ai < len(A):
        if A[ai] == B[bi]:
            ai += 1
            bi += 1
            if bi == len(B):
                bi = 0
                cnt += 1
            elif ai == len(A):
                ai = ai - bi + 1
                bi = 0
                cnt += 1
        else:
            ai = ai - bi + 1
            bi = 0
            cnt += 1

    print(f'#{tc}', cnt)