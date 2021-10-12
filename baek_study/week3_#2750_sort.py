# 수 정렬하기 (성공)
# https://www.acmicpc.net/problem/2750

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
    # lst.add(int(input()))

# sorted mathod 이용
lst = sorted(lst)

# 버블정렬
for i in range(N):
    for j in range(N):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

# 삽입정렬
for i in range(1, N):
    while(i > 0) & (lst[i] < lst[i-1]):
        M[i], M[i-1] = M[i-1], M[i]
        i -= 1

for i in range(N):
    print(lst[i])
