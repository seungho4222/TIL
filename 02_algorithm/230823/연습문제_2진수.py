bit = "0000000111100000011000000111100110000110000111100111100111111001100111"
n = len(bit)

# 이진수를 7칸 쪼개서 십진수로 만들기
for i in range(0, n, 7):
    # i번째 비트부터 7칸
    bit7 = bit[i:i + 7]
    base = 2  # 지수 밑
    ex = 0  # 거듭제곱
    dec = 0  # 십진수 결과값
    for j in bit7[::-1]:
        dec += (base ** ex) * int(j)
        ex += 1
    print(dec, end=' ')
print()

# int함수 사용
for i in range(0, n, 7):
    bit7 = '0b' + bit[i:i + 7]
    dec = int(bit7, 2)
    print(dec, end=' ')
print()