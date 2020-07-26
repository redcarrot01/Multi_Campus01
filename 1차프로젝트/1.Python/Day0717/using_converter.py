#1. 모듈명 import
from Day0717 import fah_converter
#2. 모듈명을 import 하면서 alias 명 설정
from Day0717 import fah_converter as conv
#3. 모듈에 속한 함수만 import
from Day0717.fah_converter import convert_c_to_f
#4. 모듈에 속한 모든 함수 import
from Day0717.fah_converter import *

#섭씨를 입력 받아서 화씨로 변환하기
#소수점 이하 둘째자리로 출력하기

print('변환하고 싶은 섭씨 온도를 입력하세요!')
temperature = float(input())

#1. 모듈명.convert_c_to_f() 함수호출
fah = fah_converter.convert_c_to_f(temperature)
#2. alising된 모듈명.convert_c_to_f() 함수 호출
fah = conv.convert_c_to_f(temperature)
#3. import된 함수 호출
fah = convert_c_to_f(temperature)

print('섭씨온도 :', temperature)
print('화씨온도 :', fah)
print('화씨온도 = {:.2f}'.format(fah))
print(say_hello('Python'))