def enQ(data):
    global rear
    if rear == Qsize - 1:  # 가득차면
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:
        return 'Q is Empty'
    else:
        front += 1
        return Q[front]


Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)
rear += 1   # enqueue = 3
Q[rear] = 3

while front != rear:    # 큐가 비어있지 않으면
    front += 1
    print(Q[front])

enQ(4)
print(deQ())
print(deQ())
front += 1
tmp = Q[front]
print(tmp)