# 동전 0
# https://www.acmicpc.net/problem/11047
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0
for i in lst[::-1]:
    if K == 0:
        break
    if i > K:
        continue
    else:
        cnt += K//i  # 현재 단위(i)의 몫
        K %= i  # 현재 단위(i)의 나머지

print(cnt)
