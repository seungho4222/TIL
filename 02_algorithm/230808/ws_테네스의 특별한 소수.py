# str함수
def itoa(d):
    s = ''
    while d > 0:
        s = chr(ord('0') + d % 10) + s
        d //= 10
    return s


# 테네스의 체(소수 판별)
is_prime = [True for _ in range(10 ** 6 + 1)]
is_prime[0], is_prime[1] = False, False
for i in range(2, int((10 ** 6) ** 0.5) + 1):
    if is_prime[i]:
        j = 2
        while i * j <= 10 ** 6:
            is_prime[i * j] = False
            j += 1

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    # 특별한 소수 카운트
    cnt = 0
    for i in range(A, B + 1):
        if is_prime[i]:
            # 소수에 D가 포함되면 카운트
            for j in itoa(i):
                if j == itoa(D):
                    cnt += 1
                    break

    print(f'#{tc}', cnt)