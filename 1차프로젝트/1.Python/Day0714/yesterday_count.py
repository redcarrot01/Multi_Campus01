'''
yesterday.txt 파일을 읽어서
'YESTERDAY', 'yesterday', 'Yesterday'
단어가 몇 번 나오는지 Counting 해보기
'''
#file open
#mode : r(read), w(write), a(append), rb, wb (binary file)
file = open('yesterday.txt','r')
#file의 내용을 읽은 값을 저장한 변수
yesterday_lyric = ''
while 1:
    line = file.readline()
    if not line:
        break
    #yesterday_lyric = yesterday_lyric + line.strip() + '\n'
    yesterday_lyric += line
    #yesterday_lyric = yesterday_lyric + line
print(yesterday_lyric)
#file 읽기 종료
file.close()
print(len(yesterday_lyric))

n_of_YESTERDAY = yesterday_lyric.upper().count('YESTERDAY')
print('Number of a word YESETERDAY ', n_of_YESTERDAY)
n_of_Yesterday = yesterday_lyric.count('Yesterday')
print('Number of a word Yesterday ', n_of_Yesterday)
n_of_yesterday = yesterday_lyric.lower().count('yesterday')
print('Number of a word yesterday ', n_of_yesterday)
