#사용자 정의 excpetion 클래스
# 음수값이 입력되었을때 예외 발생

class NegativePriceException(Exception):
    def __init__(self):
        print('Price can\'t be Negative')
        raise AttributeError

def clac_price(value):
    price = value *1000
    if price < 0:
        raise NegativePriceException
    return price
print(clac_price(100))
print(clac_price(-100))
