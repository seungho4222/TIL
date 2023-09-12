# 최대 공약수 GCD : GREATEST COMMON DIVISOR
# 최소 공배수 LCM : LEAST COMMON MULTIPLE

# 최대공약수
# a > b
def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# 유클리드 호제법
# a > b
# a, b의 최대공약수 구하기
# a와 b, a를 b로 나눈 나머지 r이 있다고 했을 때 다음이 성립
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 재귀적으로 (a, b) == (b, r)
# new_gcd(a,b) == new_gcd(b,r)
def new_gcd(a, b):
    # 종료 조건
    if b == 0:
        return a
    # 재귀 호출
    else:
        return new_gcd(b, a % b)


# 최소공배수
# a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수로 나눈 것과 같다
def lcm(a, b):
    return a * b // new_gcd(a, b)


a = 20
b = 15
print(gcd(a, b))
print(lcm(a, b))
