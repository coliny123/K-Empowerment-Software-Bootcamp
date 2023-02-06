stack = [None for _ in range(5)]  # list comprehenthion
# stack = [None, None, None, None, None]

top = -1

top = top +1
stack[top] = "커피"
top = top +1
stack[top] = "녹차"
top = top +1
stack[top] = "꿀물"
top = top +1
stack[top] = "오렌지주스"
top = top +1
stack[top] = "바닐라라떼"

print("----------Stack 내역 시작------------")
for i in range(len(stack)-1, -1, -1):
	print(stack[i])
print("----------Stack 내역 끝------------")


data = stack[top]
stack[top] = None
top = top -1
print(data)

print("----------Stack 내역 시작------------")
for i in range(len(stack)-1, -1, -1):
	print(stack[i])
print("----------Stack 내역 끝------------")