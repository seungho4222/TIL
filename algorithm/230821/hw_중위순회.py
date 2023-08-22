# 중위 순회
def inorder(t):
    global ans
    if t:
        inorder(cleft[t])
        ans += word[t]
        inorder(cright[t])    

# 테스트케이스 10개
T = 10
for tc in range(1, T+1):
    N = int(input())
    # 정점 정보
    arr = [list(input().split()) for _ in range(N)]
    # 노드번호에 해당하는 문자열 저장
    word = [0] * (N+1)
    # 부모노드 인덱스 => 왼쪽, 오른쪽 자식노드 번호
    cleft = [0] * (N+1)
    cright = [0] * (N+1)

    # 정점 정보 저장
    for i in arr:
        k = len(i)      # 정점정보 길이 (자식노드 유무에 따라 길이 다름)
        w = int(i[0])   # 부모노드
        word[w] = i[1]
        if k > 2:       # 완쪽 자식노드
            cleft[w] = int(i[2])
        if k > 3:       # 오른쪽 자식노드
            cright[w] = int(i[3])

    # 정점순서에 따른 해당정점 문자열 추출
    ans = ''
    inorder(1)
    
    print(f'#{tc} {ans}')


'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S

'''