# ATM (성공)
# https://www.acmicpc.net/problem/11399
'''
[문제 접근 방식]
두번째 줄에서 해당하는 숫자들을 리스트로 맵핑
.sort()를 이용

[배운점]
j의 범위를 i+1이라고 설정 : 중복해서 계수하는 것이 쉬워짐
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

lst.sort()

print(N)
print(lst)
sum_ = 0
result = 0

for i in range(N):
    for j in range(i+1):
        sum_ += lst[j]
        print(sum_)

print(sum_)
