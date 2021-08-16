# [구현] 주방장 도도새
'''
그리드 알고리즘이 아니고 처음부터 순서대로 받는 알고리즘!
첫번째 숫자 : 두번째 줄에서 map()으로 받는 list생성
두번째 숫자 : 총 근무시간
'''

num, minn = map(int, input().split())
lst = list(map(int, input().split()))
sum_ = 0
cnt = 0

for i in range(len(lst)):
    sum_ += lst[i]
    if sum_ > minn:
        break
    cnt += 1

print(cnt)
