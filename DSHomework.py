class Graph():
	def __init__(self, size):
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
	print("\t\t", end=" ")
	for v in range(g.SIZE):
		print("%9s" % store_ary[v][0], end=" ")
	print()
	for row in range(g.SIZE):
		print("%9s" % store_ary[row][0], end=" ")
		for col in range(g.SIZE):
			print("%8d" % g.graph[row][col], end=" ")
		print()
	print()


G1 = None
store_ary = [["gs25", 5], ["cu", 1], ["seven11", 2], ["mini_stop", 0], ["emart24", 3]]
gs25, cu, seven11, mini_stop, emart24 = 0, 1, 2, 3, 4


gSize = 5
G1 = Graph(gSize)
G1.graph[gs25][cu] = 1; G1.graph[gs25][seven11] = 1
G1.graph[cu][gs25] = 1; G1.graph[cu][seven11] = 1; G1.graph[cu][mini_stop] = 1
G1.graph[seven11][gs25] = 1; G1.graph[seven11][cu] = 1; G1.graph[seven11][mini_stop] = 1
G1.graph[mini_stop][cu] = 1; G1.graph[mini_stop][seven11] = 1; G1.graph[mini_stop][emart24] = 1
G1.graph[emart24][mini_stop] = 1

print("\t\t\t\t\t##편의점 그래프##")
print_graph(G1)

stack = []
visit_ary = []

current = 0
max_store = current
max_count = store_ary[current][1]
stack.append(current)
visit_ary.append(current)

while len(stack) != 0:
	next = None
	for vertex in range(gSize):
		if G1.graph[current][vertex] == 1:
			if vertex in visit_ary:
				pass
			else:
				next = vertex
				break
	if next != None:
		current = next
		stack.append(current)
		visit_ary.append(current)
		if store_ary[current][1] > max_count:
			max_count = store_ary[current][1]
			max_store = current
	else:
		current = stack.pop()
print(f"포켓몬빵 최대 보유 편의점(갯수) => {store_ary[max_store][0]} ({store_ary[max_store][1]}개)")