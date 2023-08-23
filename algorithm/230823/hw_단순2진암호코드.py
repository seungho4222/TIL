# 56자리 암호코드 찾기
def search():
    p = ''
    for r in range(N):
        for c in range(M - 1, 55, -1):
            if arr[r][c] == '1':
                p += arr[r][c - 55:c + 1]
                return p


# 암호코드 숫자 변환
def secret_code(p):
    result = []
    for i in range(0, 56, 7):
        bin_code = p[i:i + 7]
        result += [rule[bin_code]]
    return result


# 규칙 딕셔너리
rule = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 암호코드 추출
    code = secret_code(search())
    # 올바른 암호코드 판단
    calc1 = 0  # 홀수번째 1, 3, 5, 7
    calc2 = 0  # 짝수번째 2, 4, 6, 8
    for i in range(8):
        if i % 2 == 0:
            calc1 += code[i]
        else:
            calc2 += code[i]
    sum_calc = (calc1 * 3) + calc2
    # 10의 배수면 코드의 합 출력
    if sum_calc % 10 == 0:
        print(f'#{tc} {sum(code)}')
    else:  # 아니면 0 출력
        print(f'#{tc} 0')
