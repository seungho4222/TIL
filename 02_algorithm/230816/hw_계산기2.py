# 스택 밖에서 순위
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# 스택 안에서 순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 중위표기식
    infix = input()
    # 스택 및 탑으로 구현
    stack = [0] * N
    top = -1
    # 후기표현식 만들기
    postfix = ''
    for x in infix:
        # 숫자면 바로 추가
        if x.isdigit():
            postfix += x
        # 연산자일 경우
        else:
            # 스택이 비었거나 x가 스택의 탑보다 순위가 높을 경우
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            # x가 스택의 탑보다 순위가 같거나 낮을 경우
            elif isp[stack[top]] >= icp[x]:
                # 스택이 비거나 스택의 탑 순위가 더 낮을때까지
                while top > -1 and isp[stack[top]] >= icp[x]:
                    # 스택의 탑을 팝하여 후기표현식에 추가
                    postfix += stack[top]
                    top -= 1
                # 스택의 탑 순위가 더 낮아지면 그 위에 연산자 쌓기
                top += 1
                stack[top] = x
    # 남은 연산자 팝하여 표현식에 추가
    while top > -1:
        postfix += stack[top]
        top -= 1

    # 후기표기식 계산하기
    for x in postfix:
        # 숫자면 스택 쌓기
        if x.isdigit():
            top += 1
            stack[top] = int(x)
        # 연산자면 숫자 두개 팝하여 연산 후 스택에 쌓기
        else:
            right = stack[top]
            top -= 1
            left = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = left + right
            elif x == '*':
                top += 1
                stack[top] = left * right

    print(f'#{tc} {stack[top]}')


'''
101
9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3

'''