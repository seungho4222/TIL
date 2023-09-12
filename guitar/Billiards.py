from math import sqrt, acos, atan, cos, degrees

my_ball = (70, 20)
target = (30,100)
hall = (0, 127)

# 거리
a = sqrt(abs(70-0)**2 + abs(20-127)**2)
b = sqrt(abs(30-0)**2 + abs(100-127)**2)
c = sqrt(abs(70-30)**2 + abs(20-100)**2)

ga = degrees(atan((127-20)/70))
# print(((a**2 + b**2 - c**2) / (2*a*b)))
da = degrees(acos(((a**2 + b**2 - c**2) / (2*a*b))))
# print(da)
d = sqrt(a**2 + (b+5.73)**2 - 2*a*(b+5.73) * cos(da))

na = degrees(acos(((a**2 + d**2 - (b+5.73)**2) / (2*a*d))))

theta = ga + na
print(theta)