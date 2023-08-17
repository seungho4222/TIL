size = 10
cq = [0] * size
front = rear = 0


def enqueue(item):
    global rear
    if isFull():
        print('full')
        return
    rear = (rear + 1) % size
    cq[rear] = item


def dequeue():
    global front
    if isEmpty():
        print('empty')
        return
    front = (front + 1) % size
    return cq[front]


def isFull():
    return (rear + 1) % size == front


def isEmpty():
    return front == rear


for i in range(size):
    enqueue(i)

print(cq)
print(isEmpty())
print(isFull())

for i in range(size):
    print(dequeue(), end=' ')
print()

print(cq)
print(isEmpty())
print(isFull())


for i in range(90, 100):
    enqueue(i)

print(cq)