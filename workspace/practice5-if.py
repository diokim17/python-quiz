# if문
# if 조건 :
#     실행 명령문
# 조건에 따라서 아래 명령문 실행

weather = "비"
if weather == "비":
    print("우산을 챙기세요")

# 변수가 비 이므로 우산을 챙기세요 출력, 변수 값이 비가 아닐경우 아무런 출력 없이 실행 종료

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")

# 변수를 설정한 비, 미세먼지가 아닐 경우 아무런 출력 없이 실행 종료

weather = "맑음"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

# 변수를 설정한 비, 미세먼지가 아닐 경우 else문이 출력

weather = input("오늘 날씨는 어때요?") # input 문자열로 사용자 입력 받는 문장
if weather == "비" or weather == "눈": # 비 또는 눈이 입력 되면 아래 문장 출력
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

# 다른 예제

temp = int(input("기온은 어때요?")) # input은 기본적으로 문자열 따라서 int로 사용자가 입력한 값을 정수로 바꿔줌
if 30 <= temp:
    print("너무 더워요")
elif 15 <= temp < 30: # 15 <= temp and temp < 30 도 동일한 문장
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 15: # elif 여러번 사용 가능
    print("외투를 챙기세요")
else:
    print("너무 추워요") # -1도 가능