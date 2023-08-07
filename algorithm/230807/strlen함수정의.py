# 문자 길이 산출
def strlen(x):
    temp = x + '\\'
    i = 0
    while temp[i] != '\\':
        i += 1
    return i


print(strlen('amerika'))