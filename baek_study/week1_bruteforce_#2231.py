# 분해합
# https://www.acmicpc.net/problem/2231
'''
[문제 이해]
M의 분해합 : M과 M을 이루는 각 자리수의 합
(예. 256 = 245+2+4+5 / 216=198+1+9+8)

M의 분해합 = N
M = N의 생성자

자연수 N 주어질 때, 가장 작은 생성자는?

[문제 접근 방식]
N의 각 자릿수를 더할 때 문자열로 변환해서 더해주고 int화 해줌
'''
import sys
sys.stdin = open("input.txt")

N = int(input())
lst = []

for num in range(N, 0, -1):  # num = 245
    sumn = 0
    strN = str(num)  # "245"
    for i in strN:  # "2", "4", "5"
        sumn += int(i)  # sumn = 2+4+5
    result = num + sumn  # result = 245+2+4+5
    if result == N:
        lst.append(num)

# print(lst)
if not lst:
    print(0)
else:
    print(min(lst))
