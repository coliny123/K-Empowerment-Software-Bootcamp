def transformation(base, data):
    if data < base:
        print(number_char[data], end=" ")
    else:
        transformation(base, data//base)
        print(number_char[data % base], end=" ")
    binary_num = 0


number_char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

dec_num = int(input("10진수 입력 : "))
print("2진수 : ", end="")
transformation(2, dec_num)
print("\n8진수 : ", end="")
transformation(8, dec_num)
print("\n16진수 : ", end="")
transformation(16, dec_num)