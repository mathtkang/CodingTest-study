# [수학] 무어의 법칙
'''
[문제 접근 방식]

N으로 숫자를 받고
num = math.pow(2,N) -> 여기서는 math.pow(는 float형)가 아니라 내장함수 pow를 사용
num을 각각 한자리 씩 더해준다
'''
import sys

N = int(input())
num = pow(2, N)  # 여기서는 math.pow(는 float형)가 아니라 내장함수 pow를 사용

lst = []
for i in str(num):
    lst.append(int(i))

sum_ = 0
for i in lst:
    sum_ += i

print(sum_)
