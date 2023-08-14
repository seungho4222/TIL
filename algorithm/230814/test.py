'''
6528-*2/+
'''

stack = [0] * 100
top = -1
formula = '6528-*2/+'
for x in formula:
    if x not in '+-/*':     # 피연산자면...
        top += 1
        stack[top] = int(x)      # push(x)
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