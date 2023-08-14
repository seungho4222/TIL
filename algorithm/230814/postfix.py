'''
(6+5*(2-8)/2)
6528-*2/+
'''

# 중위표기식을 후위표기식으로 변환
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(6+5*(2-8)/2)'
formula = ''
for x in fx:
    if x not in '(+-/*)':
        formula += x
    elif x == ')':
        while stack[top] != '(':
            formula += stack[top]
            top -= 1
        top -= 1
    else:
        if top == -1 or isp[stack[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                formula += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = x
print(formula)

# 후위표기식 계산
formula = '6528-*2/+'
for x in formula:
    if x not in '+-/*':  # 피연산자면...
        top += 1
        stack[top] = int(x)  # push(x)
    else:
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if x == '+':
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 // op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
print(stack[top])
