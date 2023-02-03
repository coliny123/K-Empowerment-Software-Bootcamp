## 함수 선언 부분 ## 
def print_poly(px, tx):
    """
    다항식 프린트
    :param px: 계수를 원소로 가지는 list
    :param tx: 차수를 원소로 가지는 list
    :return: 다항식 문자열
    """
    print_poly = "P(x) = "

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        if coef >= 0:
            print_poly += "+"
        print_poly += f'{coef}x^{term} '
        term -= 1

        print_poly += f'{coef}x^{term} '
        term -= 1

    return print_poly


def calc_poly(x_val, px, tx):
    """
    다항식 산술
    :param x_val: x값 int
    :param px: 계수를 원소로 가지고 있는 list
    :param tx: 차수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 int
    """
    return_value = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        return_value += coef * x_value ** term
        term -= 1

    return return_value


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [7, -4, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_poly(px, tx))

    x_value = int(input("X 값-->"))

    print(calc_poly(x_value, px ,tx))