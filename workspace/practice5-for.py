# for 문
for waiting_no in [0,1,2,3,4]: # for waiting_no in range(5): -> 0에서 부터 5미만까지 for문을 실행해라 즉 같은 뜻
    print("대기번호 : {0}".format(waiting_no)) # 위 []에서 0부터 차례대로 waiting_no에 들어가서 출력이 되고 마지막인 4까지 출력 후에 실행 종료
# range에서 0부터가 아닌 1부터 5까지 출력하고 싶으면 range(1, 6) 이렇게 작성: (,) ,앞은 시작 번호 ,뒤는 미만 번호

# 예시
starbucks = ["harry", "ron", "albus"]
for customer in starbucks:
    print("{0}님 커피가 나왔습니다.".format(customer))

