# OX퀴즈
# https://www.acmicpc.net/problem/8958
'''
[문제 접근 방식]
한 줄당 하나의 계산이 이루어짐 => 처음에 N을 받고 그만큼 for문을 돌림
for문 안에서 print찍음
O가 연속된 숫자 만큼 점수가 올라가니까, distance변수를 설정해서 ++1로 차이가 발생하도록 함
'''
# sol1)
N = int(input())
for _ in range(N):
    ox_list = list(input())
    score = 0
    distance = 1
    for ox in ox_list:
        if ox == 'O':
            score += distance
            distance += 1
        else:
            distance = 1
    print(score)

# sol2)
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score
        else:
            score = 0
    print(sum_score)
