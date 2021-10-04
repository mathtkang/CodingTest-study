# 최댓값 (성공)
# https://www.acmicpc.net/problem/2562
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
num_lst = []
for i in range(9):
    num_lst.append(int(input()))

print(max(num_lst))
print(num_lst.index(max(num_lst))+1)
