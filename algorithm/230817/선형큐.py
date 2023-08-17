# 큐 초기화
size = 10
q = [0] * size
front = rear = -1


# 삽입 연산
def enqueue(item):
    global rear
    if isFull():
        print('full')
        return
    rear += 1
    q[rear] = item


# 삭제 연산
def dequeue():
    global front
    if isEmpty():
        print('empty')
        return
    front += 1
    return q[front]


def isFull():
    return rear == size - 1


def isEmpty():
    return front == rear


for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end=' ')
print()

print(q)
print(isEmpty())
print(isFull())  # 선형큐의 단점: 모든 원소 팝했지만 rear가 다 찼기 때문에 True 반환
