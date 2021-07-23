# 숫자의 개수

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

mul = A*B*C
print(mul)

lst = list(str(mul))
print(lst)

for i in range(10):  # i:0~9
    cnt = lst.count(str(i))
    print(cnt)
