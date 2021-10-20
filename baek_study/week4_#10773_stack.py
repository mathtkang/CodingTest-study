# 제로 (성공)
# https://www.acmicpc.net/problem/10773
'''
[문제 이해]
[문제 접근 방식]
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
