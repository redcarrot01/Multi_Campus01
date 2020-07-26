colors = ["red", "blue", "green"]
print(colors[0])
print(colors[2])
print(len(colors))
#list 0번째 엘리언트 값을 변경하기
colors[0] = 'Yellow'
print(colors)
#list에 엘리먼트를 1개씩 추가하기
colors.append('black')
print(colors)
#list의 엘리먼트 삭제하기
#remove('값'), del colors[인덱스]
colors.remove('black')
print(colors)
del colors[0]
print(colors)
#list에 엘리먼트를 여러개 추가하기
colors.extend(['orange','red'])
print(colors)

#지정하는 인덱스에 item을 삽입하기
colors.insert(1,'Yellow')
print(colors)

names = ['python','java','scalar','java']
#리스트의 연산
print(names * 2)
print(colors + names)
# in 구문 - 해당값이 있으면 True, 없으면 False
print('java' in names)
print('kotlin' in names)
print('python' not in names)
#해당값이 몇개 있는지를 카운팅 하기
print(names.count('java'))

print(colors)
#slicing 사용해서 삭제하기
del colors[:2]
print(colors)

#값으로 index 찾기
print(colors.index('red'))

