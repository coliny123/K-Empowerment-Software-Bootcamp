## 클래스와 함수 선언 부분 ##
class Node():
	def __init__(self):
		self.data = None
		self.link = None


def printNodes(start):
	current = start
	if current == None:
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


## 메인 코드 부분 ##
if __name__ == "__main__":
	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	printNodes(head)
	print(node.data)  # 마지막 노드인 지효가 node 라서 node.data는 마지막 노드의 데이터를 나타냄



# 딕셔너리의 키값은 포켓몬 이름 벨류는 체력 2차원리스트로 안쪽리스트에 문자열
