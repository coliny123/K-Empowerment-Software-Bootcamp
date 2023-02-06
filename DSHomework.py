class Node():
    def __init__(self):
        self.data = None
        self.plink = None
        self.nlink = None


def print_node(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 : ", end=" ")
    print(current.data, end=" ")
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=" ")
    print()
    print("역방향 : ", end=" ")
    print(current.data, end=" ")
    while current.plink != None:
        current = current.plink
        print(current.data, end=" ")


head, current, pre, = None, None, None
memory = []
twice = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :
    node = Node()
    node.data = twice[0]
    head = node
    memory.append(node)

    for once in twice[1:]:
        pre = node
        node = Node()
        node.data = once
        pre.nlink = node
        node.plink = pre
        memory.append(node)

print_node(head)