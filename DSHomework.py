import random
from math import sqrt


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_node(start):
    current = start
    if current == None:
        return
    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], "편의점 거리", sqrt(x ** 2 + y ** 2))
    print()


def sort_stores(store):
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    node_x, node_y = node.data[1:]
    node_dist = sqrt(node_x ** 2 + node_y ** 2)
    head_x, head_y = head.data[1:]
    head_dist = sqrt(head_x ** 2 + head_y ** 2)

    if head_dist > node_dist:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        curr_x, curr_y = current.data[1:]
        curr_dist = sqrt(curr_x ** 2 + curr_y ** 2)
        if curr_dist > node_dist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


head, current, pre = None, None, None
memory = []

if __name__ == "__main__" :
    names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    tuple_array = []
    for name in names:
        tuple_array.append((name, random.randint(1, 100), random.randint(1, 100)))

    print(tuple_array)

    for store in tuple_array:
        sort_stores(store)

    print_node(head)