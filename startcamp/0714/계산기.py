## 계산기 프로그램

# 사용할 수 있는 연산자
# + - * /
# % : 나누고 난 나머지
# // : 몫

# 계산기는 먼저 두 숫자를 입력받는다.
# 그 뒤에 연산자를 입력받는다. => 나누기 연산자를 입력받았다면 => 계산을 하지 않고 메세지 출력
# 연산자를 입력 받고 계산 처리
# 결과를 출력

# 한번 계산이 끝나고 또 계산을 이어 나갈 수 있도록 반복문을 사용해서 코드 작성

# 계산기를 끝내는 조건
# ex) 두 숫자 모두 0을 입력하면 종료

# 반복문 while / for
# 반복이 언제 끝날지 모르겠다 ==> while
# 반복이 언제 끝날지 예상이 된다 ==> for

# 계산기 반복 시작
# input() 으로 입력한 값은 모두 문자열로 취급
# int() 함수로 문자열을 숫자(정수)로 바꿈
# float() 함수로 문자열을 실수로 바꿈

# text to ascii <== 알파벳 콘솔 로고

print("""
.------.------.------.------.------.------.------.------.------.------.
|C.--. |A.--. |L.--. |C.--. |U.--. |L.--. |A.--. |T.--. |O.--. |R.--. |
| :/\: | (\/) | :/\: | :/\: | (\/) | :/\: | (\/) | :/\: | :/\: | :(): |
| :\/: | :\/: | (__) | :\/: | :\/: | (__) | :\/: | (__) | :\/: | ()() |
| '--'C| '--'A| '--'L| '--'C| '--'U| '--'L| '--'A| '--'T| '--'O| '--'R|
`------`------`------`------`------`------`------`------`------`------'                                                                                                                                       
""")

while True:
    a = int(input("첫 번째 숫자를 입력하세요.: "))
    b = int(input("두 번째 숫자를 입력하세요.: "))
    print("연산자는 + - * / 만 입력할 수 있습니다.")
    calc = input("연산자를 입력하세요.: ")
    if calc == "+":
        print(f"{a} {calc} {b} = {a + b}\n")
    elif calc == "-":
        print(f"{a} {calc} {b} = {a - b}\n")
    elif calc == "*":
        print(f"{a} {calc} {b} = {a * b}\n")
    elif calc == "/":
        if b == 0:
            print("0으로는 나눌 수 없습니다.\n") # 주의해야 할 점 : 나눗셈은 0으로 나누기 불가능
        else:
            print(f"{a} {calc} {b} = {a / b:.2f}\n")
    else:
        print("해당 연산자는 사용할 수 없습니다.")

    if a == b or a == 0:
        print("종료")
        break # 반복문을 종료하는 키워드

# 더 생각해 볼 수 있는 것들
# 글자를 계산할 수는 없다 ==> 사용자가 잘못 입력했을 경우 에러 처리
# 계산할 수 없는 연산자 입력
