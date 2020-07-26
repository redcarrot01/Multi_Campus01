# mode를 설정하지 않으면 default가 r(read)
# myfile = open('i_have_a_dream.txt')
# contents = myfile.read()
# print(contents)
# myfile.close()

# with 구문 사용
with open('i_have_a_dream.txt') as my_file:
    contents = my_file.read()
    word_list = contents.split(' ')
    line_list = contents.split('\n')

print('Total Number of characters : ', len(contents))
print('Total Number of words', len(word_list))
print('Total Number of lines', len(line_list))
