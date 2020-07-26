# my_file = open('count_log.txt', 'w', encoding='utf8')
# for i in range(1, 11):
#     data = '%d번째 줄\n' % i
#     my_file.write(data)
# my_file.close()

import os
#log 디렉토리가 없으면 log 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')


with open('log/count_log.txt', 'a', encoding='utf8')as f:
    for i in range(100, 111):
        data = '%d 번째 \n' % i
        f.write(data)



