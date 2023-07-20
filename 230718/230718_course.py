# 진법 변경
print(bin(12)) # 0b10 == 2
print(oct(12)) # 0o30 == 24
print(hex(12)) # 0x10 == 16

# 유한 정밀도
print(2 / 3)
print(5 / 3)

# 실수 연산시 해결책
a = 3.2 - 3.1
b = 1.2 - 1.1
print(abs(a - b) <= 1e-10)
import math
print(math.isclose(a,b))

# 지수(제곱하는 횟수) 표현 10^
print(314e-2) # 3.14
print(314e2) # 31400.0
print(314 * 10 ** 2) # 31400

# f-string
bugs = 'roaches'
counts = 100
area = 'living room'
print(f"Debugging {bugs} {counts} {area}")
# print("Debugging {} {} {}".format(bugs, counts, area))
# print("Debugging %s %d %s" % (bugs, counts, area))

# f-string 응용
gretting = 'hi'
print(f'{gretting:>10}')
print(f'{gretting:^10}')
print(f'{3.141592:.4f}')

# 불변과 가변
my_str = 'hello'
# my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list) # [100, 2, 3]


x = 10
y = x

x = 20
print(x) # 20
print(y) # 10

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3]


a = [1, 2, 3]
b = a
print(a is b)


vowels = 'aeiou'
print(('a' and 'b') in vowels) # ()안의 값의 str은 모두 True이므로 결국 vowels에 b가 있는지 확인
print(('b' and 'a') in vowels) # ()안의 값의 str은 모두 True이므로 결국 vowels에 a가 있는지 확인
print(('b' in vowels) and ('a' in vowels)) # vowels에 'b'와 'a'가 있는지 확인
