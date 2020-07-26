'''
섭씨를 입력 받아서 화씨로 변환하기
소수점 이하 둘째자리로 출력하기
'''
print('변환하고 싶은 섭씨 온도를 입력하세요!')
temperature = float(input())

fah = ((9/5) * temperature ) + 32
print('섭씨온도 :', temperature)
print('화씨온도 :', fah)
print('화씨온도 = {:.2f}'.format(fah))