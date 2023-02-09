# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요.
"""
print(sentence3)

# 슬라이싱
jumin = "990406-1234567"

print("성별 : " + jumin[7]) # 컴퓨터는 0부터 시작 따라서 앞의 9는 0번째 자리로 계산
print("연 : " + jumin[0:2]) # : 범위 설정 단, 항상 끝 값은 미만이므로 2번째 자리 미만이라고 생각
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6]) # 처음부터 시작할 때는 [:6]이라고 적어도 무방
print("뒤 7자리 : " + jumin[7:]) # [7:14] 와 동일한 값, 끝나는 값이 마지막자리 이므로 위와 동일
print("뒤 7자리 (뒤에서 부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 소문자 출력
print(python.upper()) # 대문자 출력
print(python[0].isupper()) # python에 있는 변수의 첫번째 값이 대문자인가? => 참/거짓 구분
print(len(python)) # python 전체 문자열의 길이
print(python.replace("Python", "Java")) # python에 있는 변수 중 Python이라는 문자를 찾아서 Java로 바꾸어 출력

# index: 배열에서 값의 위치를 찾아주는 함수, 중복된 값이 있으면 가장 최소의 위치를 리턴
# index(value, start, end)
# a = "423456" 일 때,
# a 문자열에서 4의 위치 찾기: print(a.index("4"))
# a 문자열 중 3번째 자리부터 마지막 자리까지에서 4의 위치 찾기: ptrint(a.index("4",2,5))
index = python.index("n") # python에 있는 변수 중 n이라는 문자가 어디에 있는지 알려줌
print(index)
index = python.index("n", index + 1) # n이 있는 자리 5에서 1을 더한 6번째 자리부터 또 n이 나오는 위치 찾기 즉, 두번째 n찾기
print(index)

print(python.find("n")) # 31번과 같은 결과 값 출력
print(python.find("Java")) # -1 출력, 원하는 값이 변수에 포함되어 있지 않을 경우에는 -1 반환
'''
print(python.index("Java")) # 37번과 달리 반환하는 값 없이 오류가 남 = ValueError: subtring not found
# 38번에서 오류 발생 따라서 프로그램이 종료가 되므로, 이후에 어떤 식을 작성해도 출력 x 
'''
print(python.count("n")) # python에 있는 변수 중 n이 몇번 등장하는가

# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # % 뒤에 있는 값을 %d 자리에 넣겠다. 단 d는 정수를 의미 따라서 항상 정수 값만 넣을 수 있음
print("나는 %s을 좋아해요" % "파이썬") # %s는 문자열 string 값
print("Apple 은 %c로 시작해요" % "A") # %c는 한 글자만 character 값
# %s는 정수, 문자 상관없이 다 출력
print("나는 %s살입니다." % 20) # 49번과 동일한 값 출력
print("나는 %s색과 %s색을 좋아해요" % ("초록", "검정")) # ()를 통해 하나 이상의 값 입력 가능, "," 순서대로 입력

# 방법 2
print("나는 {}살 입니다." .format(20)) # format()안의 값을 {}안에 들어감
print("나는 {}색과 {}색을 좋아해요" .format("초록", "검정")) # 하나 이상의 값 가능
print("나는 {0}색과 {1}색을 좋아해요" .format("초록", "검정")) # 0번째 == 초록, 1번째 == 검정
print("나는 {1}색과 {0}색을 좋아해요" .format("초록", "검정")) # 초룍, 검정 순서 변경
# {}만 사용: 연속적으로 값 출력, {}안에 숫자: 그 순번에 맞게 출력

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color ="초록"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color ="초록", age = 20)) # {}안에 변수 적어주면 format에서 변수 순서가 달라도 상관없다.

# 방법 4 (v3.6 이상)
age = 20
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
'''
print("백문이 불여일견 
      백견이 불여일타")
위 문장은 오류 발생
따라서 옳은 문장은
'''
print("백문이 불여일견 \n백견이 불여일타") # \n은 줄바꿈 단, 실제로 작성시에는 \n으로 값 출력시에 줄바꿈으로 출력

'''
저는 "Dio Kim"입니다. 이렇게 출력하고 싶으면
print("저는 "Dio Kim"입니다")
위 문장은 오류 발생
따라서 옳은 문장은
'''
print("저는 'Dio Kim'입니다") # 방법 1
print('저는 "Dio Kim"입니다') # 방법 2 
# 87번과 88번 차이는 Dio Kim을 '',"" 
# 단 방법 2와 같이 시용하려면 ''로 문장을 시작해야 하는 헷갈림 발생 가능 이때 탈출 문자 사용
print("저는 \"Dio Kim\"입니다") # \"내용\" 방법 2와 같은 문장 출력 \'내용\'은 방법 1과 같은  문장 출력, 즉 문장 내에서 따옴표 역할

# \\: 문장 내에서 \ 출력
# print("c:\python\workspace\practice3.py") 오류 발생, \+문자 형태는 탈출문자 형태임 따라서 올바른 탈출문자 형태도 아니기 때문에 오류 발생
print("c:\\python\\workspace\\practice3.py")

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine") # \r 뒤의 Pine 4글자를 맨 앞으로 이동 따라서 "Red "의 4개의 자리에 Pine이 들어옴 즉, 문자가 대체되는 것

#\b: 백스페이스 (한글자 삭제)
print("Redd\bApple") # \b 바로 앞 문자 지움

# \t: 탭 역할
print("Red\tApple")

# Quiz
# 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# 따라서 생성된 비밀번호: nav51!

'''
내가 작성한 코드
url = "http://naver.com"
# print("제외된 부분 " + url[7:12])
password = url[7:12] 
firstpw = password[:3] 
secondpw = len(password)
thirdpw = password.count("e")
print("생성된 비밀번호: "+ str(firstpw) + str(secondpw) + str(thirdpw) + "!")
# 출력 결과: nav51!
# 오직 naver만 가능한 프로그램 따라서 적용 불가
'''

# 올바른 코드
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2, my_str이라는 변수에 들어있는 문자열 중에서 처음부터 처음 나오는 .의 위치 직전까지 자른다
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))
# naver 뿐만 아니라 다른 url주소도 가능 