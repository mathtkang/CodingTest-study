# 수학은 비대면강의입니다.
# https://www.acmicpc.net/problem/19532
'''
[문제 접근 방식]
'''
import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i, j)
