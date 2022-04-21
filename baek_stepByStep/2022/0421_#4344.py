# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
'''
[문제 접근 방식]
한 줄당 하나의 계산이 이루어짐 => 처음에 N을 받고 그만큼 for문을 돌림
아래 단계를 한줄씩 실행
(1) 평균을 구한다
(2) 평균보다 높은 학생들의 비율을 구한다.
    1) 평균보다 높은 학생 수 구함
    2) 비율을 구함
'''
# sol1)
c = int(input())

for _ in range(c):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]  # (1)평균을 구함 (n[0]: 학생수, n[1:] 점수)
    student_cnt = 0  # (2)-1)평균 이상인 학생 수
    for score in n[1:]:
        if score > avg:
            student_cnt += 1

    rate = (student_cnt/n[0])*100  # (2)-2)비율을 구함
    print(f'{rate:.3f}%')  # 반올림, 소수점 셋째 자리까지
