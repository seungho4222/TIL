hex1 = '0F97A3'
hex2 = '01D06079861D79F99F'


def solution(hex_string):
    # 16진수 문자열을 2진수 문자열로 바꾸면 길이 * 4
    l = len(hex_string) * 4

    # 16진수 문자열을 숫자로 바꾸기
    x = int(hex_string, 16)

    # 7칸씩 잘라서 이진수로 만든 뒤에 이진수 출력
    # 이진수를 10진수로 바꾸고 출력
    for i in range(l - 1, -1, -7):
        # 현재 위치 i에서 7개 잘라서 이진수 만들어서 출력
        # 이진수로 바꾼 결과 문자열
        bin_string = ''
        for j in range(7):
            if i - j < 0:
                break
            bin_string += '1' if x & (1 << i - j) else '0'

        print(bin_string, end=': ')
        dec = int(bin_string, 2)
        print(dec, end=' ')
    print()


solution(hex1)
solution(hex2)