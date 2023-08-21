class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

root = A
A.left = D
A.right = E
E.left = B
E.right = C


def preorder(T):
    if T:
        print(T)
        preorder(T.left())
        preorder(T.right())


preorder(A)
