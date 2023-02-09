# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 나머지 구하기 1
print(5//3) # 몫 구하기 1
print(10//3) # 몫 구하기 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # == 앞과 뒤가 같다 즉, 등호 따라서 True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # != 같지 않다 따라서 True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # and는 앞의 조건와 뒤의 조건이 모두 만족할 시 True
print((3 > 0) & (3 < 5)) # and == & 따라서 True

print((3 > 0) or (3 > 5)) # or는 앞의 조건과 뒤의 조건 중 하나라도 참이면 True 출력 따라서 True
print((3 > 0) | (3 > 5)) # or == | 따라서 True (|는 shift \)

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20 ()안 우선 순위 적용
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16  
print(number)
number += 2 # 18  39번 문장과 같은 뜻 
print(number)

# 41번 응용
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)
number %= 2 # 0  2를 나눈 나머지를 구하라 
print(number)

number = 16
number %= 5 # 1  5를 나눈 나머지를 구하라
print(number)

# 숫자 처리 함수
print(abs(-5)) # 5  abs는 절댓값
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12  입력 받은 2개의 값 중 큰 값 출력
print(min(5, 12)) # 5  입력 받은 2개의 값 중 작은 값 출력
print(round(3.14)) # 3  반올림
print(round(4.99)) # 5

from math import * # math 라이브러리 안에 있는 모든 것을 이용하겠다
print(floor(4.99)) # 4 내림 
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근 

# 랜덤 함수
from random import *

print(random()) # 난수 출력 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 즉, 범위 안의 정수 값 출력
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# 이를 활용하여 로또 값 출력해보기
# print(int(random() * 40) + 5) # 내가 생각한 답 
# 수정 후
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) 
print(int(random() * 45) + 1)
print(int(random() * 45) + 1) 
print(int(random() * 45) + 1) 
print(int(random() * 45) + 1) 

# 위의 내용을 더 쉽게 작성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성 즉 1 <= x < 46
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 즉 1 <= x <= 45
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))

# Quiz
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1. 랜덤으로 날짜를 뽑아야 함
# 조건 2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3. 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제 
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# 수정 전
# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")

# 수정 후
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")

# random 함수를 내장하고 있지 않으므로 모듈함수를 선언해야 함