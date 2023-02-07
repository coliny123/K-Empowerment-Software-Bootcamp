def is_queue_full():
    global SIZE, rear, front, queue
    if (rear+1 % SIZE) == front:
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
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def dequeue():
    global SIZE, rear, front, queue
    if is_queue_empty():
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def cal_times():
    global SIZE, rear, front, queue
    time = 0
    for i in range((front + 1) % SIZE, (rear + 1) % SIZE):
        time += queue[i][1]
    return time


SIZE = 6
rear = front = 0
queue = [None for _ in range(SIZE)]

if __name__ == "__main__":
    waiting = [("민지", 9), ("혜린", 3), ("하니", 4), ("혜인", 4), ("다니엘", 3)]
    for i in waiting:
        print(f"대기 예상 시간 : {cal_times()} 분 입니다.")
        print(f"현재 대기 중 => {queue}\n")
        enqueue(i)

    print(f"최종 대기 명단 => {queue}")
    print("예약 마감!")

