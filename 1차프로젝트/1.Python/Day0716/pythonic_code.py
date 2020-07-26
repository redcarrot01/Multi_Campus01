# # join() 함수 : list -> str
# colors = ['red', 'yellow','green']
# result = ' '.join(colors)
# print(result)
# result = '/'.join(colors)
# print(result)
#
# # split() 함수 : str -> list
# langs = 'python,java,c#,sclar'
# result = langs.split(',')
# print(type(result), result)
# a,b,c,d = langs.split(',')
# print(a,b,c)
#
# langs = 'python java c# sclar'
# # 공백으로 구분하는 문자열인 경우에는
# # split() 함수에서 구분자를 주지 않아도 된다.
# result = langs.split()
# print(result)
#
# # 일반적인 for loop
# my_list = []
# for val in range(10):
#     if val % 2 == 0:
#         my_list.append(val)
# print(my_list)
#
# # 1. List Comprehension (포괄적인 리스트)
# my_list2 = [val for val in range(10)]
# print(my_list2)
#
# my_list3 = [val for val in range(10) if val % 2 == 0]
# print(my_list3)
#
# my_list4 = [val if val % 2 == 0 else 10 for val in range(10)]
# print(my_list4)
#
# # 2. 문자열 타입 list comprehension
# word1 = 'Hello'
# word2 = 'World'
# # for i in word1:
# #     for j in word2:
# #         print(i+j)
# my_list5 = [i+j for i in word1 for j in word2]
# print(my_list5, len(my_list5))
#
# my_list = [i+j for i in word1 for j in word2 if i != j]
# print(my_list, len(my_list))
#
# words = 'Yesterday love was such an easy game to play'.split()
# #print(words)
#
# word_lists = []
# for w in words:
#     word_list = [w.upper(), w.lower(), len(w)]
#     word_lists.append(word_list)
# #print(word_lists)
#
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# print(stuff)
#
# for word_list in stuff:
#     print(word_list)
#
# # indexed traversal
# langs_list = 'python java c# sclar'.split()
# # Bad
# for idx in range(len(langs_list)):
#     print(f'idx = {idx}, value={langs_list[idx]}')
#
# # Good - enumerate() 함수
# for idx, lang in enumerate(langs_list):
#     print(f'idx={idx}, value={lang}')
#
# print(enumerate(langs_list))
# print(list(enumerate(langs_list)))
#
# # Dict Comprehension
# my_dict = {idx:val.capitalize() for idx,val in \
#            enumerate('Yesterday love was such an easy game to play'.split())}
# print(my_dict)
#
# print(dict(enumerate(langs_list)))
#
# # Variable Exchange
# a = 10
# b = 20
# # bad
# tmp = a
# a = b
# b = tmp
#
# a = 100
# b = 200
# # good
# a, b = b, a
# print(a, b)
# # Sequence UnPacking
# a, *rest = [1, 2, 3]
# print(a, rest)
#
# a, *middle, c = [1, 2, 3, 4]
# print(a, middle, c)
#
# # Judgement T, F
# # Bad
# attr = True
# if attr == True:
#     pass
# # Good
# if attr:
#     pass
#
# attr = None
# # Bad
# if attr == None:
#     pass
# # good
# if attr is None:
#     pass
#
# # zip() 함수
# a, b, c = zip((1,2,3),(10,20,30),(100,200,300))
# print(a,b,c)
#
# for val in zip((1,2,3),(10,20,30),(100,200,300)):
#     print(type(val))
#
# # index가 같은 값을 tuple로 묶어서 합을 계산하고 List에 저장함
# sum_list = [sum(val) for val in zip((1,2,3),(10,20,30),(100,200,300))]
# print(sum_list)
#
# # Enumerate & Zip
# a_list = ['a1','a2','a3']
# b_list = ['b1','b2','b3']
# for i, (a,b) in enumerate(zip(a_list, b_list)):
#     print(i, a, b)

######################################################################
##pythonic code practice 0726
#1. split 함수 -> 문자열의 값을 나누어 리스트 형태로 반환
items = 'zero one two three'.split() #공백기준으로 문자열 나눔
print(type(items), items)
# => <class 'list'>, ['zero', 'one', 'two', 'three']

langs= 'python, java, three'
a,b,c = langs.split(",")
print(a,b,c)
# => python  java  three

url = 'mail.naver.com'
subdomain,domain,type = url.split(".")
print(subdomain,domain,type)
# => mail naver com

#2. join함수 -> string list를 합쳐 하나의 문자열로 반환
colors = ['red', 'yellow', 'green']
result = ''.join(colors)
print(result)
# -> redyellowgreen

#3. list comprehension
# 기존 리스트 사용하여 간단히 다른 리스트 만들기
# for + append 보다 속도 빠름

result = []
for i in range(10):
    result.append(i)
print(result)
# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in range(10) if i%2 == 0]
print(result)
# => [0, 2, 4, 6, 8]

word_1 = "Hello"
word_2 = "Hello"
result = [i+j for i in word_1 for j in word_2]
print(result)
# => ['HH', 'He', 'Hl', 'Hl', 'Ho', 'eH', ...]
result = [i+j for i in word_1 for j in word_2 if not(i==j)]
print(result)
# => ['He', 'Hl', 'Hl', 'Ho', 'eH', 'el'...]

words = 'Yesterday love was such an easy game to play'.split()
print(words)
# => 리스트로 반환 ['Yesterday', 'love', 'was', 'such' ...]

word_lists = []
for w in words:
    word_list = [w.upper(), w.lower(), len(w)]
    word_lists.append(word_list)
print(word_lists)
# => [['YESTERDAY', 'yesterday', 9], ['LOVE', 'love', 4]...]

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
# => [['YESTERDAY', 'yesterday', 9], ['LOVE', 'love', 4]...]

for word_list in stuff:
    print(word_list)
# => ['YESTERDAY', 'yesterday', 9]
# ['LOVE', 'love', 4]
# ['WAS', 'was', 3] ...


