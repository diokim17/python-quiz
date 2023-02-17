# continue 와 break
# -> 반복문 내에서 사용

# 상황
# 선생님이 교실에서 학생들에게 책을 읽으라고 지시할 때 (1번 읽어봐, 2번 읽어봐 같은 식)
# 근데 2명이 결석했다고 가정

absent = [2, 5] # 2번과 5번이 결석, 따라서 제외하고 다음 번호가 이어서 읽을 때 -> continue 사용
for student in range(1, 11): # 1번부터 10번까지 있다고 가정
    if student in absent:
        continue
    print("{0}번 책 읽어보세요".format(student))

# 결과: 2, 5 제외해서 출력

absent = [2, 5] # 2번과 5번이 결석, 따라서 제외하고 다음 번호가 이어서 읽을 때 -> continue 사용
no_book = [7] # 결석은 아니나 책을 놓고 왔다고 가정
noise = [9] # 수업시간에 시끄럽게 했을 때 수업을 그냥 끝낸다고 가정
for student in range(1, 11): # 1번부터 10번까지 있다고 가정
    if student in absent:
        continue # continue를 만나면 continue 기준으로 아래 문장 실행x, 다음 번호 반복
    elif student in no_book:
        print("{0}번은 뒤로 나가고 쉬는 시간에 교무실로 따라 오도록".format(student))
        continue
    elif student in noise:
        print("오늘 수업은 여기까지 하고, {0}번은 따라와".format(student))
        break # break와 동시에 더이상 진행x, 반복문 탈출
    print("{0}번 책 읽어보세요".format(student))
