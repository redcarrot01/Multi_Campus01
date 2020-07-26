'''
input() 함수를 사용해서 사용자로 부터 입력 값을 받겠다.
'''
print('이름을 입력하세요')
name = input()
print(type(name))
print('Hello' , name )

print('온도를 입력하세요!')
temperature = float(input())
print(type(temperature))
print('입력한 온도 값은 : ', temperature)
