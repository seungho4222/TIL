# 1과 자기 자신만을 약수로 가지는 수
# prime number

# 어떤 숫자 n이 소수인지 소수가 아닌지
# 1부터 n까지 다 나눠보고 나누어 떨어진 횟수가 2개보다 많으면 소수가 아님
# 2부터 n-1까지 다 나눠보고 나누어 떨어진적이 한번이라도 있으면 소수가 아님

prime = []
for i in range(2, 1000):
    # i가 소수인지 아닌지 판별
    # 소수이면 prime 에 추가
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

'''
에라토스테네스의 체
2부터 소수를 구하고자 하는 구간의 모든 수를 나열
처음 시작할 때 2부터 모든 수가 소수라고 가정
2부터 소수 판별 시작하는데 2는 소수에 해당
소수인 수들은 자기 자신을 제외한 배수를 모두 소수가 아니라고 체크
체크가 안되있는 다음 수로 이동
위의 과정을 반복
'''
n = 1000  # 2부터 1000까지의 모든 수에 대하여 소수 판별
is_prime = [True for i in range(n + 1)]  # is_prime[i] => 숫자 i가 소수인가? 소수면 True, 아니면 False

for i in range(2, int(n ** 0.5) + 1):  # 2부터 n의 제곱근까지만 확인
    if is_prime[i]:  # i가 소수인 경우
        # i를 제외한 모든 i의 배수를 소수가 아니라고 체크
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1

print(is_prime[501])
