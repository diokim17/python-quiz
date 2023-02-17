# for 문
for waiting_no in [0,1,2,3,4]: # for waiting_no in range(5): -> 0에서 부터 5미만까지 for문을 실행해라 즉 같은 뜻
    print("대기번호 : {0}".format(waiting_no)) # 위 []에서 0부터 차례대로 waiting_no에 들어가서 출력이 되고 마지막인 4까지 출력 후에 실행 종료
# range에서 0부터가 아닌 1부터 5까지 출력하고 싶으면 range(1, 6) 이렇게 작성: (,) ,앞은 시작 번호 ,뒤는 미만 번호

# 예시
starbucks = ["harry", "ron", "albus"]
for customer in starbucks:
    print("{0}님 커피가 나왔습니다.".format(customer))

# 한줄 for문
# 상황
# 출석번호 1번, 2번,...이 있었는데, 100번부터 시작으로 변경 -> 101, 102,.. 이런식
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 또 다른 예제
# 학생 이름을 길이로 변환
students = ["harry", "voldmote", "malfoy"] # 현재 이름은 문자열 이 문자열을 길이 즉, harry는 5글자 이므로 5 이렇게 변경
students = [len(i) for i in students] # len: 어떤 문자열의 값이나 길이를 의미
print(students)

# 또 다른 예제
# 학생 이름을 대문자로 변환
students = ["harry", "voldmote", "malfoy"]
students = [i.upper() for i in students]
print(students)

# ()안에 변수를 넣는지, 변수.을 하는 건지 구분!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!