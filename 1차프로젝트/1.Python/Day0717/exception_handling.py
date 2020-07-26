# try_~except ~else
# try ~except ~finally

for i in range(10):
    # result =0
    try:
        result = 10/i #지역변수
    except ZeroDivisionError as err:
        # 어떨때 어떤 예러 -> Exception써도 무방
        print(err)
    else:
        print(result)
    finally:
        print('종료되었음')

