# abstract method를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name
    #추상 메서드
    def talk(self):
        raise NotImplementedError('자식클래스에서 반드시 구현해야 함')

class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return 'Woof'
    def pet(self):
        return 'im pet'

my_ani = Animal('동물')#이거해도 에러안나
print(my_ani)
# my_ani.talk() #이건 에러남 추상 메서드를 호출하면 예외 발생

animals = [Cat('고양이'), Dog('강아지1'), Dog('강아지2')]
for ani in animals:
    print(ani.talk())
   # print(ani.pet())


class Mywallet(object):
    def __init__(self, money):
        self.money = money

    @property #같은 money이지만 @에 의해 다른 역할
    def money(self):
        return self._money

    @money.setter #얘를 명시하지 않으면 read-only
    #외부에서 값을 변경할 수 없음
    def money(self, money):
        self._money = money


s = Mywallet('5000')
print(s.money)
s.money ='10000'
print(s.money)

# 기존에 money 함수에 인자를 넣으면 새터로,
# 그냥 호출하면 게터로