## 클래스와 함수 선언 부분 ##
class Node():
	def __init__(self):
		self.data = None
		self.link = None

	# def __repr__(self):
	# 	return f"Node__repr__"


def printNodes(start):
	current = start
	if current == None:
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()


def insert_node(find_data, insert_data):
	global head, current, pre

	if head.data == find_data:  # 첫 번째 노드 삽입
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link != None:  # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == find_data:
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()  # 마지막 노드 삽입
	node.data = insert_data
	current.link = node


def delete_node(delete_data):
	global head, current, pre

	if head.data == delete_data:
		print("# 첫 노드가 삭제됨 #")
		current = head
		head = head.link
		del current
		return

	current = head
	while current.link != None:
		pre = current  		    # 이전 current는 pre가 됨
		current = current.link  # current가 한칸씩 증가
		if current.data == delete_data:
			print("# 중간 노드가 삭제됨 #")
			pre.link = current.link
			del current
			return
	# 삭제할 데이터를 못찾을 경우 함수 종료
	print("# 삭제된 노드가 없음 #")


def find_nodes(find_data):
	global head, current, pre

	current = head
	if current.data == find_data:
		return current

	while current.link != None:
		current = current.link
		if current.data == find_data:
			return current
	return Node()



## 전역 변수 선언 부분 ##
#memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]


## 메인 코드 부분 ##
if __name__ == "__main__":
	node = Node()		# 첫 번째 노드
	node.data = data_array[0]
	head = node
	#memory.append(node)

	for data in data_array[1:]:	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		#memory.append(node)

	printNodes(head)
	#print(node.data)  # 마지막 노드인 지효가 node 라서 node.data는 마지막 노드의 데이터를 나타냄
	insert_node("피카츄", "잠만보")
	printNodes(head)
	insert_node("파이리", "어니부기")
	printNodes(head)
	insert_node("성윤모", "거북왕")
	printNodes(head)

	delete_node("잠만보")
	printNodes(head)
	delete_node("어니부기")
	printNodes(head)
	delete_node("강찬석")
	printNodes(head)

	print(find_nodes("파이리").data)
	print(find_nodes("박민석").data)




# 딕셔너리의 키값은 포켓몬 이름 벨류는 체력 2차원리스트로 안쪽리스트에 문자열
