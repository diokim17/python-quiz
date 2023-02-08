# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
# 문자열과 숫자를 혼합해서 사용 가능

# boolean 자료형
# 참과 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

# 변수: 어떤 값을 저장하는 공간
# 애완동물을 소개해 주세요
print("우리집 강아지 이름은 짱아에요")
print("짱아는 17살이고, 강아지 평균 수명은 15살이에요")
print("그럼 짱아는 노견일까요? True")

# 같은 문장을 변수를 사용하여 작성
animal = "강아지"
name = "짱아"
age = 17
avgage = 15
is_adult = age >= 7

'''
배우기 전 나의 코딩
print("우리집" animal "의 이름은" name"이에요")
print(name"는" age"살이며," animal "평균 수명은" avgage"살이에요")
print("그럼" name"는" is_adult"?")
'''

# 수정 후
print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는" + str(age) + "살이며,"  + animal + "평균 수명은"  + str(avgage) + "살이에요") #str: 정수형을 문자형으로 바꿔주는 역할
print(name, "는", age, "살이며,", animal, "평균 수명은", avgage, "살이에요") #49번째 줄과 같은 문장 단, str 없이 변수 그대로 사용 가능
print("그럼" + name + "는 노견일까요?" + str(is_adult))
'''
49번 50번 비교
+ 는 정수형을 str 붙여야 print 출력 가능
, 는 정수형을 그대로 사용 가능하지만, 띄어쓰기가 기본 옵션임
'''

#Quiz
# 다음 변수를 이용하여 다음 문장을 출력하시오
# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : xx 행 열차가 들어오고 있습니다.

station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")
