# 6장- 6.1- 제어 변수의 활용

##다음 3가지는 같은 출력
###1
for x in range(1, 51):
    if(x%10 == 0):
        print('+', end='')
    else:
        print('-', end='')
print('\n')
###2
for x in range(1, 6):
    print('-'*9, end='')
    print('+', end='')
print('\n')
###3
x=1
while x<=50:
    if x%10:
        print('-', end='')
    else:
        print('+', end='')
    x +=1

## 6.2- 이중루프- 별그리기
for y in range(1, 10):
    for x in range(y) :
        print('*', end='')
    print()
#y라는 제어변수 안쪽에서 바깥쪽 참조함

## 6-2- 무한루프
# 반복횟수 알 수없을때 조건 참조하여 탈출하는 형식
while True:
    a = int(input())
    if(a==7): break

     