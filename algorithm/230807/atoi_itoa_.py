# 숫자리스트 -> 문자 변환
d = [1,2,3]
d = ''.join(list(map(str, d)))
print(d)    # 123 -> class 'str'


# int()와 같은 atoi()함수 만들기
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

s = '123'
print(atoi(s))  # 123 -> class 'int'


# str()과 같은 itoa()함수 만들기
def itoa(a):
    s = ''
    while a > 0:
        s = chr(ord('0') + a % 10) + s  # 1의자리 숫자의 ASCII값
        a //= 10
    return s

a = 123
print(itoa(a))  # 123 -> class 'str'



# ord() : 문자열을 아스키코드로 반환    -> ord('a') == 97
# chr() : 아스키코드를 문자열로 반환    -> chr(65) == A