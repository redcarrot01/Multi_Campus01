import os
import sys
# python directory_handling.py log/count_log.txt
                 #0                   #1
#디렉토리가 없으면 log 디렉토리 생성
if not os.path.isdir("log"):
    os.mkdir("log")

if len(sys.argv) >= 2:
    file_name = sys.argv[1]
    print(file_name)

    print('file write start')
    #log/count_log.txt 파일이 존재하지 않으면
    if not os.path.exists(file_name):
        f = open(file_name, 'w', encoding="utf8")
        f.write("기록이 시작됩니다\n")
        f.close()

    with open(file_name, 'a', encoding="utf8") as f:
        import random, datetime
        for i in range(1, 11):
            stamp = str(datetime.datetime.now())
            value = random.random() * 1000000
            log_line = stamp + "\t" + str(value) +" 값이 생성되었습니다\n"
            f.write(log_line)
    print('file write ends')
else:
    print('enter file name')
