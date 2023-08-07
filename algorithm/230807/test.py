def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i


s = '123'
a = atoi(s)
print(a + 1)


def itoa(x):
    s = ''
    while x > 0:
        s += chr(ord('0') + x % 10)  # 1의자리 숫자의 ASCII코드
        x //= 10
    return s


a = 123
print(itoa(a))
