T = int(input())
for tc in range(1, T+1):
    word = input()
    # 괄호 짝 올바르면 1, 아니면 0 출력
    answer = 1
    stack = []
    for i in word:
        if not len(stack):
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' or i == '}':
                answer = 0
                break
        else:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ')' or i == '}':
                answer = 0
                break
    if len(stack):
        answer = 0
    print(f'#{tc}', answer)

'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

'''