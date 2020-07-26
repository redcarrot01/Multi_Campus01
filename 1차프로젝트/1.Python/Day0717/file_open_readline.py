#readline()함수 사용
with open('i_have_a_dream.txt', 'r') as my_file:
    #line number
    i =0
    while True:
        line = my_file.readline()
        if line.strip() !="": #공백 줄
            print(str(i) + '==='+ line.strip())
        if not line:
            break
        i = i+1