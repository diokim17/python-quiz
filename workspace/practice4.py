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
# 리스트와는 다르게 변경이나 추가 불가능 따라서 변경되지 않는 목록을 사용할 때 사용
# 대신에 리스트 보다는 속도가 빠름
menu = ("fanta", "coke")
print(menu[0])
print(menu[1])

# 활용
# name = "apple"
# color = "red"
# kind = "fruit"
# print(name, color, kind)

name, color, kind = "apple", "red", "fruit"
print(name, color, kind) # 113번과 동일한 결과 값

# 세트(set), 집합
# 중복 x, 순서 x
my_set = {1, 2, 3, 3, 3} # {}는 위에 사전(55번 줄)에서도 사용 -> key, value를 사용, set에서는 값만 나열하면 됨
print(my_set) # 중복x 따라서 {1, 2, 3} 출력

pro_java = {"harry", "ron", "hermione"}
pro_python = set(["voldmote", "harry"])
# 교집합 (java, python 모두 할 수 있는 자)
print(pro_java & pro_python) # {'harry'} 출력
print(pro_java.intersection(pro_python)) # 동일하게 교집합인 {'harry'} 출력, intersection = 교집합
print(pro_python.intersection(pro_java)) # 125번과 동일하게 출력

# fruit_red = {"apple", "tomato", "cherry"}
# fruit_green = {"apple", "melon"}
# print(fruit_red & fruit_green) # {'apple'} 출력 위의 코드처럼(122~125) 교집합 출력

# 합집합 (java, python 할 수 있는 자)
print(pro_java | pro_python) # 중복x 따라서 {'hermione', 'voldmote', 'harry', 'ron'} harry는 중복이므로 한번만 출력, 또한 순서x 따라서 내가 적은 코드 순서와 무관하게 출력
print(pro_java.union(pro_python)) # 133번과 동일하게 출력, union = 합집합
print(pro_python.union(pro_java)) # 133번과 동일하게 출력

# 차집합 (java 가능한자, python 불가능한자)
print(pro_java - pro_python) # {'hermione', 'ron'} 출력
print(pro_java.difference(pro_python)) # 139번과 동일하게 출력

# python 할 수 있는자 추가
pro_python.add("ron")
print(pro_python) # {'voldmote', 'harry', 'ron'} 출력, 튜플과 다르게 추가 가능함

print(pro_java.intersection(pro_python)) # 교집합, 따라서 {'ron', 'harry'} 출력

# java 까먹은자
pro_java.remove("ron")
print(pro_java) # {'harry', 'hermione'} 출력, 제거도 가능함


# 자료구조의 변경
# 커피숍이라면
drink = {"latte", "americano", "juice"}
print(drink, type(drink)) # class 'set'으로 출력, {}로 문자 감싸져 있음, class는 practice8 참고

drink = list(drink)
print(drink, type(drink)) # class 'list'로 출력, []로 문자 감싸져 있음

drink = tuple(drink)
print(drink, type(drink)) # class 'tuple'로 출력, ()로 문자 감싸져 있음

drink = set(drink)
print(drink, type(drink)) # class 'set'으로 출력, {}로 문자 감싸져 있음

# Quiz
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1: 편의상 댓글은 20명이 작성하였고, 아이디는 1 ~ 20 이라고 가정
# 조건 2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 활용 예제
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))



