T = int(input())
for tc in range(1, T+1):
    word = input()
    # 괄호 짝 올바르면 1, 아니면 0 출력
    answer = 1
    stack = []
    for i in word:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if not len(stack):
                answer = 0
                break
            a = stack.pop()
            if not((a == '(' and i == ')') or (a =='{' and i =='}')):
                answer = 0
                break
    if len(stack):
        answer = 0
    print(f'#{tc} {answer}')