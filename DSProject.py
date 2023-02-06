## 클래스와 함수 선언 부분 ##
import random


class Node():
	def __init__(self):
		self.data = None
		self.link = None

	# def __repr__(self):
	# 	return f"Node__repr__"


def print_nodes(start):
	current = start
	if current.link == None:
		return
	print(current.data, end = ' ')
	while current.link != start:  #
		current = current.link
		print(current.data, end = ' ')
	print()


def insert_nodes(find_data, insert_data):
	global head, current, pre

	if head.data == find_data:  # 첫 번째 노드 삽입
		node = Node()
		node.data = insert_data
		node.link = head
		last = head
		while last.link != head:   # 원형linkedlist는 head로 끝까지 돌았는지 판단 선형linkedlist는 None으로
			last = last.link   #
		last.link = node  #
		head = node  #
		return

	current = head
	while current.link != head:  # 중간 노드 삽입
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
	node.link = head  #


def delete_nodes(delete_data):
	global head, current, pre

	if head.data == delete_data:
		print("# 첫 노드가 삭제됨 #")

		current = head
		head = head.link
		last = head
		while last.link != current:
			last = last.link
		last.link = head
		del current
		return

	current = head
	while current.link != head:  # 원형linkedlist는 head로 끝까지 돌았는지 판단 선형linkedlist는 None으로
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

	while current.link != head:  # 원형linkedlist는 head로 끝까지 돌았는지 판단 선형linkedlist는 None으로
		current = current.link
		if current.data == find_data:
			return current
	return Node()


def count_plus_minus_zero():
	# odd_even = count_odd_even()  # False가 리턴
	global head, current, pre

	plus, minus, zero = 0, 0, 0

	# SRP(단일 책임의 원칙) 위배
	# if head == None:
	# 	return False

	current = head
	while True:
		if current.data > 0:
			plus += 1
		elif current.data < 0:
			minus += 1
		else:
			zero += 1

		if current.link == head:
			break
		current = current.link
	return plus, minus, zero


def make_toggle_number(plus, minus, zero):
	current = head
	while True:
		current.data *= - 1
		if current.link == head:
			break
		current = current.link


## 전역 변수 선언 부분 ##
#memory = []
head, current, pre = None, None, None
data_array = list()

## 메인 코드 부분 ##
if __name__ == "__main__":
	for _ in range(7):
		data_array.append(random.randint(-100, 100))

	node = Node()		# 첫 번째 노드
	node.link = head
	node.data = data_array[0]
	head = node  #
	#memory.append(node)

	for data in data_array[1:]:	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head  #
		#memory.append(node)

	print_nodes(head)
	plus_minus_zero = count_plus_minus_zero() #False가 리턴
	print(f"plus : {plus_minus_zero[0]}, minus : {plus_minus_zero[1]}, zero : {plus_minus_zero[2]}")
	make_toggle_number(plus_minus_zero[0], plus_minus_zero[1], plus_minus_zero[2])
	print_nodes(head)