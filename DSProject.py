def is_stack_full():
	global SIZE, stack,top
	if top >= SIZE -1:
		return True
	return False


def is_stack_empty():
	global SIZE, stack,top
	if top == -1:
		return True
	return False


def push(data):
	global SIZE, stack, top
	if is_stack_full():
		print("stack is FULL!!")
		return
	top = top + 1
	stack[top] = data


def pop():
	global SIZE, stack, top
	if is_stack_empty():
		print("stack is EMPTY~")
		return
	temp = stack[top]
	stack[top] = None
	top -= 1
	return temp


def peek():
	global SIZE, stack, top
	if is_stack_empty():
		print("stack is EMPTY~")
		return None
	return top


SIZE = int(input("stack size : "))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__" :
	while True:
		select = input("삽입(i)/추출(e)/확인(v)/종료(x) 중 하나를 선택 ==> ").lower()
		if select == 'x':
			break
		elif select == 'i':
			data = input("input data ==> ")
			push(data)
			print("stack status : ", stack)
		elif select == 'e':
			data = pop()
			print("extrated data ==> ", data)
			print("stack status : ", stack)
		elif select == 'v':
			data = peek()
			print("check data ==> ", data)
			print("stack status : ", stack)
		else :
			print("input mismatch")

	print("program end!")
