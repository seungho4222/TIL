T = int(input())
for tc in range(1, T+1):
    # 십진수 실수 입력
    num = float(input())
    # 이진수 출력값: '0.' 빼고
    bin_string = ''
    # 이진수 만들기
    while num != 0:
        # 13자리 이상이면 브레이크
        if len(bin_string) >= 13:
            break
        # 2곱해주고 1의자리 수 더해주기
        num *= 2
        # 1넘으면 1의자리 수 입력하고 빼주기
        if num >= 1:
            bin_string += '1'
            num -= 1
        else:
            bin_string += '0'
    # 13자리 넘으면 오버플로우
    if len(bin_string) >= 13:
        print(f'#{tc} overflow')
    # 아니면 2진수 출력
    else:
        print(f'#{tc} {bin_string}')
