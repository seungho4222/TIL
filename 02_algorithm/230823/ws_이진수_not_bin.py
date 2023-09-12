T = int(input())
for tc in range(1, T+1):
    # N: 자리수, hexadecimal: N자리 16진수
    N, hexadecimal = input().split()
    print(f'#{tc}', end=' ')
    # 16진수 각자리 순회
    for i in range(int(N)):
        decimal = int(hexadecimal[i], 16)
        if decimal == 0:
            print('0000', end='')
            continue
        temp = ''
        while decimal > 0:
            if decimal == 1:
                temp = '1' + temp
                break
            temp = str(decimal % 2) + temp
            decimal //= 2
        print(f'{int(temp):04d}', end='')
    print()


'''
3
4 47FE
5 79E12
8 41DA16CD

'''