# 2869 달팽이는 올라가고 싶다.
# https://www.acmicpc.net/problem/2869

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
N = 0
for i in range(V):
    N += A
    if N >= V:
        print(i+1)
        break
    N -= B

# 위와 같이 작성시 : 시간초과


while 1:
    N += 1
    if N*A - (N-1)*B >= V:
        print
