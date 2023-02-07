def is_queue_full():
    global SIZE, rear, front, queue
    if rear == SIZE-1:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, rear, front, queue
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global SIZE, rear, front, queue
    if is_queue_full():
        print("queue is full")
        return None
    else:
        rear += 1
        queue[rear] = data


def dequeue():
    global SIZE, rear, front, queue
    if is_queue_empty():
        print("queue is empty")
        return None
    else:
        front += 1
        data = queue[front]
        queue[front]= None

        for i in range(front +1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front = -1
        rear -= 1

        return data


SIZE = 5
rear = front = -1
queue = [None for _ in range(SIZE)]

if __name__ == "__main__":
    enqueue("민지")
    enqueue("혜린")
    enqueue("하니")
    enqueue("혜인")
    enqueue("다니엘")

    for i in queue:
        if is_queue_empty():
            print("식당 영업 종료!")
        else:
            print(f"대기줄 상태 : {queue}")
            print(f"{dequeue()} 님 식당에 들어감")
