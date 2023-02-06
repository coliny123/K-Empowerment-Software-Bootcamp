def is_stackempty():
    global SIZE, song, top
    if top == -1:
        return True
    else:
        return False


def is_stackfull():
    global SIZE, song, top
    if top >= SIZE-1:
        return True
    else:
        return False


def push(data):
    global SIZE, song, top
    if is_stackfull():
        return
    top += 1
    song[top] = data


def pop():
    global SIZE, song, top
    if is_stackempty():
        return
    data = song[top]
    song[top] = None
    top -= 1
    return data


SIZE = 100
song = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    with open("애국가.txt", "r", encoding="utf8")as rfp:
        lyrics_array = rfp.readlines()

    print("------original------")
    for line in lyrics_array:
        push(line)
        print(f"{line}", end=" ")
    print()

    print("------reverse------")
    while True:
        line = pop()
        if line == None:
            break

        small_stack = [None for _ in range(len(line))]
        small_top = -1
        for ch in line:
            small_top +=1
            small_stack[small_top] = ch

        while True:
            if small_top == -1:
                break
            ch = small_stack[small_top]
            small_top -=1
            print(f"{ch}", end= "")

