# 리스트: 순서를 가지는 객체의 집합
# 예) 지하철 칸 별로 10명, 20명, 30명이 있을 때
subway1 = 10
subway2 = 20
subway3 = 30
# 위와 같이 작성, 위의 변수를 하나로 작성할 수 있다
subway = [10, 20, 30] # subway 리스트 안에 10, 20, 30 값이 차례로 들어감
print(subway)

subway = ["Herry", "Hermione", "Ron"] # 순서는 0 1 2
print(subway)

# 활용
# Herry가 몇번 째 칸에 있는가
print(subway.index("Herry")) # 1

# 다음 정류장에서 다음 칸에 "Bill" 탑승
subway.append("Bill") # append: 뒤에 더하다 따라서 맨 뒤에 붙음
print(subway)

# Hermione와 Ron 사이에 탑승 즉, 0 1 2 3에서 2번 자리에 와야 함
subway.insert(2, "Voldmote")
print(subway)

# 뒤에서 한명 씩 제거
print(subway.pop())
print(subway)
# print(subway.pop()) 반복하면 계속 한명 씩 제거

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("Ron")
print(subway)
print(subway.count("Ron"))

# 정렬
num_list = [5, 3, 1, 4, 2]
num_list.sort() # 작은 순서대로 정렬
print(num_list) 
num_list.reverse() # 위의 정렬된 순서를 반대로 53142 라면 24135, .sort로 정렬 후 .reverse 사용이라면 54321
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list) # 출력 결과: [] 대괄호는 출력 됨

# 다양한 자료형과 함께 사용
mix_list = ["Hery", 20, True]
print(mix_list)

# 리스트 확장
ex_list = [1, 3, 4, 2]
ex_list.extend(mix_list)
print(ex_list)

# 사전 dictionary = {key : value} 특정 key와 value를 한 쌍을 이루게 해 순서와 상관없이 key를 이용해 바로 value에 접근
# key에 대한 중복은 허용 불가
# 사물함으로 예시
cabinat = {3:"Herry", 100:"Hermione"}
print(cabinat[3])
print(cabinat[100])
print(cabinat.get(3)) # 59번 줄과 같은 값 출력
# print(cabinat[5]) # 오류 Key Error 5, 따라서 프로그램 종료로 Hi 출력 불가
print(cabinat.get(5)) # Key 5가 없어도 프로그램 종료는 되지 않으나 None 값 출력
print(cabinat.get(6, "Available")) # 없는 값의 Key가 입력되면 None대신 ""안에 문구 출력
print("Hi")

# 사전 자료형 안에 값의 유무 확인 있으면 참, 없으면 거짓
print(3 in cabinat) # True
print(5 in cabinat) # False

# 정수가 아닌 문자열도 가능
locker = {"A-1":"Voldmote", "B-2":"Ron"}
print(locker["A-1"])
print(locker.get("B-2"))
print("A-1" in locker)
print("A-2" in locker)

# 새로운 쌍 추가
print(locker)
locker["C-23"] = "Albus" # 새로운 쌍 추가
locker["A-1"] = "Malfoy" # 기존 쌍 변경 Voldmote -> Malfoy
print(locker)

# 기존 쌍 삭제
del locker["B-2"]
print(locker)

# Key들만 출력
print(locker.keys())

# Value들만 출력
print(locker.values())

# Key, Value 쌍으로 출력
print(locker.items())

# 사전 제거
locker.clear()
print(locker) # 결과: {} {}만 출력

# 튜플

# 세트
# 자료구조의 변경
# Quiz