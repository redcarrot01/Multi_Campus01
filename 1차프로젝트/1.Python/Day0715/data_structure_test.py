# Stack - LIFO(last in first out)
my_stack = [20,10,30,40,20]
print(my_stack)
my_stack.append(100)
print(my_stack)
my_stack.pop()
print(my_stack)
# Queue - FIFO(first in first out)
my_stack.pop(0)
print(my_stack)
my_stack.append(30)
print(set(my_stack))

my_tuple = tuple(my_stack)
print(type(my_tuple), my_tuple)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 50
print(my_tuple * 2)
print(len(my_tuple))

my_int = (1)
print(type(my_int), my_int)
my_tuple2 = (1,)
print(type(my_tuple2), my_tuple2)

#Set
my_set = set([40,20,49,50,20,50])
print(my_set)
my_set.add(49)
print(my_set)
my_set.remove(49)
print(my_set)
my_set.discard(20)
print(my_set)

my_set.add(60)
my_set.add(30)
print(my_set)
# discard() 함수는 해당 값이 존재하지 않더라고 에러를 발생시키지 않는다.
my_set.discard(10)
print(my_set)

#  remove() 함수는 해당 값이 존재하지 않으면 KeyError를 발생시킨다.
# KeyError: 10
# my_set.remove(10)

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
# 합집합
print(s1.union(s2))
print(s1 | s2)
# 교집합
print(s1.intersection(s2))
print(s1 & s2)
# 차집합
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)

#Dict
my_dict = {}
my_dict2 = dict()
print(type(my_dict), type(my_dict2))
my_dict['java'] = '자바'
my_dict['python'] = '파이썬'
my_dict['java script'] = '자바스크립트'
print(my_dict)
print(my_dict['java'])
# 매칭되는 key값이 없으면 KeyError 발생한다.
#print(my_dict['python1'])
# 매칭되는 key값이 없으면 에러 발생하지 않고 None 을 반환한다.
print(my_dict.get('python1'))
value = my_dict.get('python1')
if value is None:
    print('해당 Key가 존재하지 않습니다.')

if value:
    print(value)
else:
    print('해당 Key가 존재하지 않습니다.')
# 해당 key 삭제
del my_dict['python']
print(my_dict)
# in 구문을 사용해서 해당 key 있는지를 체크한다.
print('java' in my_dict)

#keys(), values() , items()
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict)

print(my_dict)
#매칭되는 key가 없으면 추가해 준다.
my_dict.setdefault('python','파이썬')
my_dict.setdefault('java','자바2')
print(my_dict)