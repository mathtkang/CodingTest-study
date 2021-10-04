# [그리디] 거스름돈 (성공)
# https://www.acmicpc.net/problem/5585
'''
어떤 동전을 얼만큼 거슬러주는지는 상관 X
동전의 개수가 몇 개인지가 중요!
'''
N = 1000-int(input())  # 받은 돈
cnt = 0  # 동전 개수
lst = [500, 100, 50, 10, 5, 1]  # 거스름돈 종류

for i in lst:
    cnt += N//i
    N %= i  # 나머지

print(cnt)
