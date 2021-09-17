# [수학] 무어의 법칙
'''
[문제 접근 방식]

N으로 숫자를 받고
num = math.pow(2,N)
num을 각각 한자리 씩 더해준다
'''
import sys
import math
input = sys.stdin.readline

N = int(input())
num = math.pow(2, N)

lst = []
for i in str(num):
    lst.append(i)
    print(i)
