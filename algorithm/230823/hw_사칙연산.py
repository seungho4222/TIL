# 중위순회
# 괄호 확인용
check = 0
def inorder(t):
    global infix, check
    if t:
        inorder(cleft[t])
        # 정점번호가 짝수이면 여는 괄호 추가
        if t % 2 == 0 and arr[t] not in '+-/*':
            infix += ['(']
            check += 1
        infix += [arr[t]]
        # 정점번호가 홀수이면 닫는 괄호 추가
        if t % 2 == 1 and arr[t] not in '+-/*' and check != 0:
            infix += [')']
            check -= 1
        inorder(cright[t])

# 중위표현식 -> 후기표현식 변경
icp = {'(': 3, '*': 2, '/':2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/':2, '+': 1, '-': 1}
def postfix(infix):
    postfix_arr = []
    stack = [0] * N
    top = -1
    for i in infix:
        if i not in '(+-/*)':
            postfix_arr += [i]
        elif i == ')':
            while stack[top] != '(':
                postfix_arr += [stack[top]]
                top -= 1
            top -= 1
        else:
            if top == -1 or isp[stack[top]] < icp[i]:
                top += 1
                stack[top] = i
            elif isp[stack[top]] >= icp[i]:
                while top > -1 and isp[stack[top]] >= icp[i]:
                    postfix_arr += [stack[top]]
                    top -= 1
                top += 1
                stack[top] = i
    while top > -1:
        postfix_arr += [stack[top]]
        top -= 1
    return postfix_arr


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 인덱스를 노드번호로 하는 정점의 값
    arr = [0] * (N+1)
    # 인덱스를 부모노드로 하는 자식노드
    cleft = [0] * (N+1)
    cright = [0] * (N+1)
    # 정점 정보 저장
    for i in range(N):
        node = list(input().split())
        num = int(node[0])
        # 정점 값 저장
        arr[num] = node[1]
        # 자식노드 저장
        if node[1] in '+-/*':
            cleft[num] = int(node[2])
            cright[num] = int(node[3])
    # 중위순회로 중위표기식 추출
    infix = []
    inorder(1)
    print(infix)
    print(postfix(infix))
    # 중위표현식을 후기표현식으로 변경하고 계산
    stack = [0] * N
    top = -1
    for i in postfix(infix):
        if i not in '+-/*':
            top += 1
            stack[top] = int(i)
        else:
            right = stack[top]
            top -= 1
            left = stack[top]
            top -= 1
            if i == '+':
                top += 1
                stack[top] = left + right
            elif i == '-':
                top += 1
                stack[top] = left - right
            elif i == '/':
                top += 1
                stack[top] = left / right
            elif i == '*':
                top += 1
                stack[top] = left * right
    
    print(f'#{tc} {int(stack[top])}')


'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65

7
1 / 2 3
2 - 4 5
3 - 6 7
4 261
5 61
6 81
7 71

#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2
'''