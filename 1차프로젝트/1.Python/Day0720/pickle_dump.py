import pickle

# 사용자로부터 문자열을 몇번 입력할지를 숫자로 입력 받는다
number_of_Data = int(input('enter the number of data:'))
# 입력 받은 데이터를 저장할 리스트 선언
data = []

# 입력 받은 숫자만큼 for loop으로 문자열을 입력을 받는다
for idx in range(number_of_Data):
    raw = input('enter data'+str(idx)+':')
    data.append(raw)

# pickle의 dump()를 이용해서 문자열을 저장한 리스트를 저장한다
file = open('important', 'wb')
pickle.dump(data, file)
file.close()