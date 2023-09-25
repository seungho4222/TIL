T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 암호 숫자 자릿 수
    P = input()  # N자리 16진수
    k = input()  # 한자리 16진수 키
    d_k = int(k, 16)  # 키를 10진수로 변경

    result = ''  # 출력값
    for i in P:  # 16진수의 각 자릿수 확인
        d = int(i, 16)  # 10진수로 변경
        d_k_xor = d^d_k  # 변경한 수와 키의 XOR값 출력
        ans = hex(d_k_xor)[2:]  # xor값을 16진수로 변경 후 진수 정보 제거
        if ans.islower():
            result += ans.upper()  # 문자면 대문자로 변경
        else:
            result += ans  # 숫자는 그냥 추가
    print(f'#{tc} {result}')
