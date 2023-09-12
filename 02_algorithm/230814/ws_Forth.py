def get_result(postfix):
    stack = []
    for c in postfix:
        if c == '.':
            if len(stack) == 1:
                return stack[0]
            else:
                return 'error'
        elif c not in '+-/*.':
            stack += [int(c)]
        else:
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
                if c == '+':
                    result = left + right
                elif c == '-':
                    result = left - right
                elif c == '/':
                    result = left // right
                elif c == '*':
                    result = left * right
                stack += [result]
            else:
                return 'error'


T = int(input())
for tc in range(1, T + 1):
    postfix = input().split()
    print(f'#{tc}', get_result(postfix))

'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

'''
