'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

N = int(input())
tree = list(map(int, input().split()))

# 인덱스가 부모노드의 번호
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

for i in range(N - 1):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c


# 전위순회: V - L - R
def preorder(t):
    if t:
        print(t, end=' ')
        preorder(cleft[t])
        preorder(cright[t])


# 중위순회: L - V - R
def inorder(t):
    if t:
        inorder(cleft[t])
        print(t, end=' ')
        inorder(cright[t])


# 후위순회: L - R - V
def postorder(t):
    if t:
        postorder(cleft[t])
        postorder(cright[t])
        print(t, end=' ')


preorder(1)
print()
inorder(1)
print()
postorder(1)
