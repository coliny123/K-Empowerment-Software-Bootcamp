import random


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


root = None
song_list = ["Hype-Boy", "Ditto", "Attention", "Cookie", "OMG", "Next Level", "Savage"]
request_list = [random.choice(song_list) for _ in range(20)]

print(f"오늘 신청된 곡(중복ㅇ) : {request_list}")

node = TreeNode()
node.data = request_list[0]
root = node

for name in request_list[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

print("이진 탐색 트리 구성 완료!")


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(f"{node.data}", end=" ")
    inorder(node.right)


print("오늘 신청된 곡 (중복x) : ", end=" ")
inorder(root)