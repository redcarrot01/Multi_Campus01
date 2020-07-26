# SoccerPlayer 클래스 선언
class SoccerPlayer(object):
    # 생성자 선언 - 객체가 생성될때 자동으로 호출되는 함수
    def __init__(self, name, position, back_number):
        #access modifier 가 public
        self.name = name
        self.position = position
        self.back_number = back_number

    # 일반함수 (instance method), back_number 값을 입력받아서 변경하는 함수
    # 함수의 첫번째 파라미터에 self 가 있어야 클래스에 속한 함수가 됩니다. 
    # 첫번째 파라미터의 이름은 self 가 아니어도 괜찮음
    def change_back_number(self, new_number):
        print(f'선수의 등번호를 변경합니다. \
        from {self.back_number} to {new_number}')
        self.back_number = new_number

    # toString() 메서드와 동일한 역할
    # 객체의 주소가 아니라 객체가 가진 특정 인스턴스 값을 출력
    def __str__(self):
        return f'My Name is {self.name}, I Play in {self.position} in center'

def main():
    # 객체생성
    dooly = SoccerPlayer('둘리','MF',10)
    print(dooly)
    print(dooly.__str__())

    print('현재 선수의 등번호는 {}'.format(dooly.back_number))
    dooly.change_back_number(5)
    print('변경된 선수의 등번호는 {}'.format(dooly.back_number))
#main()
