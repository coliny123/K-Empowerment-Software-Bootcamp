import random


def is_stackempty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False


def is_stackfull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False


def push(data):
    global SIZE, stack, top
    if is_stackfull():
        return
    top += 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stackempty():
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    stone_color = ["주황", "초록", "파랑", "보라", "빨강", "노랑"]
    random.shuffle(stone_color)

    print("Way to cookie_house : ", end=" ")
    for stone in stone_color:
        push(stone)
        print(f"{stone} => ", end=" ")
    print("Cookie_house\n")

    print("Way to home : ", end=" ")
    for stone in stack:
        data = pop()
        print(f"{data} => ", end=" ")
    print("Home\n")



