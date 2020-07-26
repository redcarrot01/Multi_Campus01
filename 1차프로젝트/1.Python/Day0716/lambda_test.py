# 일반적인 함수 정의
def add(x, y):
    return x + y
print(add(10, 20))
# lambda 함수 정의
add2 = lambda x, y: x + y
print(add2(100,200))

#제곱승, 곱하기, 나누기 람다함수로 정의해서 호출
my_pow = lambda x: x ** 2
print(my_pow(2))
print((lambda x: x ** 2)(3))

my_div = lambda x: x / 2
print(my_div(10))

my_arr = [1,2,3,4,5]
result = map(lambda x: x * 2, my_arr)
print(result)
print(list(result))

result = list(map(lambda x: x * 2, my_arr))
print(result)

#  [1,2,3,4,5]
#+ [1,2,3,4,5]
#   2,4,6,8,10
# add(1,1)  add(2,2)  add(3,3)
f_add = lambda x,y: x + y
print(f_add(1,1))
result = list(map(f_add, my_arr, my_arr))
print(result)

# my_arr 리스트의 값을 제곱승 해서 다른 리스트에 저장하세요
# lambda 함수와 map() 함수 사용합니다
f_pow = lambda x: x**2
result = map(f_pow, my_arr)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

#filter 함수
result = filter(lambda x: x > 2, my_arr)
print(result)
print(list(result))

for val in filter(lambda x: x > 2, my_arr):
    print(val)

# reduce
# functools.py 라는 모듈안에 있는 reduce 함수를 불러오기
from functools import reduce
result = reduce(lambda x, y: x+y, my_arr)
print(result)
