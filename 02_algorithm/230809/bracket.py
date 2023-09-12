T = int(input())
for tc in range(1, T+1):
    row = input()   # 괄호의 짝이 맞는지 검사할 문자열

    stack = []  # 스탯

    answer = 1  # 짝이 맞으면 1, 아니면 0 출력

    # 괄호 검사
    # row 에서 한글자씩 가져와서 검사
    # 가져온 글자가 만약 여는 괄호다? => 스택에 삽입
    # 떼어낸 글자가 닫는 괄호다 => 스택에서 하나 꺼내온 다음에
    # 짝이 맞는지 검사
    # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!!

    # 모든 글자 검사가 끝난 후에 스택에 비어있지 않으면 오류!!

    for i in row:
        if not len(stack):
            if i == '(':
                stack.append(i)
            elif i == ')':
                answer = 0
                break
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
    if len(stack):
        answer = 0

    print(f'#{tc}', answer)
