import sys
# sys.stdin = open('input.txt', 'r')
# input을 어떻게 받아야할지 모르겠다!
# 5 // test case
# 5 50 50 70 80 100 // 1번째 원소는 학생 수
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
test = int(input())

for _ in range(test):
    input_list = list(map(int, sys.stdin.readline().split()))
    # 전체 값 입력 받아서 student_list로 복사하기
    student_num = input_list[0]
    
    score_list = input_list[1:]
    
    avg_score = sum(score_list) / student_num
    count = 0
    for score in score_list :
        if score > avg_score:
            count += 1
            
    print("{:.3f}%".format(float(count / student_num) * 100))