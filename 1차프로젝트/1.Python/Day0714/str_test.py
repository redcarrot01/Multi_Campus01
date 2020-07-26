#문자열 처리
greet = ('\n' + 'Hello') * 4
print(greet)
print(greet + greet )
print("I like 'Apple' ")
print('I like \'Python\'')

my_int = 100
flag = True
print(type(my_int), type(flag))
result = str(my_int) + str(flag)
print(type(result), result)

#문자열 인덱스
greeting = 'HELLO WORLD!'
print(greeting[1])
print(greeting[11])
#print(greeting[12])

#문자열 Slicing
print(greeting[2:5])
print(greeting[5:])
print(greeting[:5])
print(len(greeting))

#str 의 여러가지 함수들 사용하기
word = 'GOOD manufacturing Practice'
print(word.upper())
print(type(word.split(' ')), word.split(' '))
#str -> list : packing
my_wordlist = word.split(' ')
print(my_wordlist)
word_list = list(word)
print('list() 함수 ', word_list)
#list -> str : unpacking
str1, str2, str3 = my_wordlist
print(str1)
print(str2)
print(str3)

#packing
my_list = ['a','b','c',]
#unpacking
a1, a2, a3 = my_list
print(a1)
print(a2)
print(a3)
#print(a4)

#word = word.upper()
#print(word)

print(word.title())
print(word.capitalize())



