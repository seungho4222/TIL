T = int(input())
for tc in range(1, T+1):
    # N: 자리수, hexadecimal: N자리 16진수
    N, hexadecimal = input().split()
    print(f'#{tc}', end=' ')
    # 16진수 각자리 순회
    for i in hexadecimal:
        # 10진수 변경
        decimal = int(i, 16)
        # 2진수 변경 후 0b 삭제
        binary = bin(decimal)[2:]
        # 4자리수 맞춰주기
        while len(binary) < 4:
            binary = '0' + binary
        print(binary, end='')
    print()
