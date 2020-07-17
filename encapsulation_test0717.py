#product 클래스 선언
class Product(object):
    #생성자
    def __init__(self,name) :
        # __name 이 private 변수
        self.__name = name

    def __str__(self):
        return 'Product의 이름은{}'.format(self.__name)

    @property
    def name(self):
        return self.__name

    #property밑에 와야 함
    @name.setter
    def name(self, name):
        self.__name = name

#Attributer error :
#객체 생성
#getter 함수 호출해야 동작함
product = Product('tv')
print(product.name)

#setter 함수 호출
#product_name('ddd')이건 안됨
#setter 붙은 경우에는  그냥 변수처럼
# 일반 변수는 위에처럼
product.name = '텔레비전'
print(product.name)
