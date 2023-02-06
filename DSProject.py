## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def makeSimpleLinkedList(namePhone) :
	global memory, head, current, pre
	printNodes(head)

	node = Node()
	node.data = namePhone
	memory.append(node)
	if head == None :			# 첫 번째 노드일 때
		head = node
		return

	if head.data[1] > namePhone[1] :	# 첫 번째 노드보다 작을 때
		node.link = head
		head = node
		return

	# 중간 노드로 삽입하는 경우
	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[1] > namePhone[1]:
			pre.link = node
			node.link = current
			return

	# 삽입하는 노드가 가장 큰 경우
	current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	for data in dataArray :
		makeSimpleLinkedList(data)

	printNodes(head)

