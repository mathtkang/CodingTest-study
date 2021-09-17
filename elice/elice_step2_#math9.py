# [수학] 버스
'''
최소공배수 구하는 문제
'''
import math
import sys
input = sys.stdin.readline

s, t = map(int, input().split())

print(math.lcm(s, t))
