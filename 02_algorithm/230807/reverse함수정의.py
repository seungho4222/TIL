# 문자열 뒤집기
def s_reverse(x):
    x_lst = list(x)
    N = len(x)
    for i in range(N//2):
        x_lst[i], x_lst[N-1-i] = x_lst[N-1-i], x_lst[i]
    return ''.join(x_lst)


print(s_reverse('Reverse'))