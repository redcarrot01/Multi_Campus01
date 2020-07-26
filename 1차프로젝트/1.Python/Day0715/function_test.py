# 평균을 계산하는 함수를 정의
def my_average(numbers):
    # local variable
    total = 0
    for num in numbers:
        total += num
    my_avg = total / len(numbers)
    return int(my_avg)

def connect(server, port):
    return 'http://{}:{}'.format(server,port)

# default parameter 로 정의한 함수
def times(n1=10, n2=20):
    return n2 - n1

# *p - tuple type parameter , 아규먼트의 갯수가 가변적
def var_param(*p):
    return p

# **p - dict type parameter ,
def var_param_dict(**p):
    print(type(p), p)
    for k,v in p.items():
        print(k, v)

def tuple_dict_param(n1, n2, *n3, **n4):
    print(n1, n2, sum(n3))
    print(n4)

# 다중값을 리턴하는 함수
def swap(a, b):
    return b, a

def main():
    prices = [1000, 3000, 2500, 450]
    result = my_average(prices)

    print(result)
    # 함수 외부에서는 local 변수를 사용할 수 없음
    # print(total)
    
    # 위치 파라미터
    result1 = connect('server.com', '9080')
    print(result1)
    # 키워드 파라미터
    result1 = connect(port='8087', server='aa.com')
    print(result1)

    result2 = times()
    print(result2)
    result2 = times(7)
    print(result2)

    result2 = times(19, 30)
    print(result2)

    result3 = var_param(1,)
    print(type(result3), result3)
    result3 = var_param(1,2,3,)
    print(result3)

    var_param_dict(n1=10, n2=20, n3=30)

    tuple_dict_param(10, 20, 100,200,300, a=10, b=20)

    result4 = swap(200, 100)
    print(type(result4), result4)
    x, y = swap(450, 230)
    print(f'x는 {x} , y는 {y}')

'''
def swap(a, b):
    return b, a
'''
main()
