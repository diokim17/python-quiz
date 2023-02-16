# while
# while (조건): 
# 조건이 만족할 때까지 반복하라

customer = "harry"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

'''
# 무한루프
customer = "ron"
index = 1
while True:
    print("{0}님 커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
    index += 1
# 무한루프에 빠졌을 때, 터미널에서 ctrl c 를 누르면 강제 종료
'''

# 예를 들어 손님을 부를 때 계속 부르는 것이 아니라 손님이 오면 확인하고 주고 아니면 부르는 식
customer = "harry"
person = "unknown"

while person != customer:
    print("{0}님 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
# input에 입력한 값이 person으로 지정, 그 person에 들은 변수가 customer와 같으면 실행 종료, 다르면 반복

'''
내가 추가해 본 코드
while, if 동시 가능

while person != customer:
    print("{0}님 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    if person != customer:
        print("아직 준비되지 않았습니다. 기다려 주세요.")
    else:
        print("{0}님 여기 있습니다. 맛있게 드세요".format(person))
'''
