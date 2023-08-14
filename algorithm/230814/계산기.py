infix = '(6+5*(2-8)/2)'
infix = '2+3*4/5'
n = len(infix)

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}


def get_postfix(infix, n):
    postfix = ''
    stack = []

    for i in range(n):
        if infix[i] not in '(+-/*)':
            postfix += infix[i]
        else:
            if infix[i] == ')':
                while stack:
                    temp = stack.pop()
                    if temp == '(':
                        break
                    postfix += temp
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()

    return postfix


# 2. 후위표기식의 결과를 계산할 함수
def get_result(postfix):
    stack = []
    for c in postfix:
        if c not in ['(', '+', '-', '/', '*']:
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

            if c == '+':
                result = left + right
            elif c == '-':
                result = left - right
            elif c == '/':
                result = left / right
            elif c == '*':
                result = left * right

            stack.append(result)
    return stack.pop()


print(get_postfix(infix, n))
print(get_result(get_postfix(infix, n)))
