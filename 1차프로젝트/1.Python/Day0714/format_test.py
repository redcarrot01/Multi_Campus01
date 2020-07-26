# 1.%formating : C언어 style
# 2. String format 함수 : {} 에 대응하는 값을 format() 의 인자로 전달
# 3.f-string : python3.6  이상에서 만 사용\

temperature = 36
print('1.온도 값은 %d %.2f' %(temperature, temperature))
print('2.온도 값은 {}'.format(temperature))
print(f'3.온도 값은 {temperature}')

#padding
print('Product {0:10s}, Price per unit {1:10.3f}'.format("Apple", 5.243))
print('Product {0:>10s}, Price per unit {1:10.3f}'.format("Apple", 5.243))
#naming
# print('Product {name:10s}, Price per unit {price:10.3f}'\
# #       .format(name:"Apple", price:5.243))
