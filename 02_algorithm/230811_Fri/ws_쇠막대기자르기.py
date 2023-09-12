T = int(input())
for tc in range(1, T+1):
    pole = input()
    cnt = 0
    ans = 0
    for i in range(len(pole)):
        if pole[i] == '(':
            cnt += 1
        else:
            if pole[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')

'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())

'''