# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
'''
[문제 접근 방식]
'''
# sol1)
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수

    rate = (cnt/nums[0])*100
    print(f'{rate:.3f}%')

# sol2)
num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]

    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1

    per = (cnt/scores[0])*100
    print('%.3f' % per + '%')
