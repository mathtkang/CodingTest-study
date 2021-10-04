# 회의실 배정
# https://www.acmicpc.net/problem/1931
'''
[문제 이해]


[힌트]
(1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다. => 튜플형태
[문제 접근 방식]
리스트와 튜플 형식으로 저장
시작숫자중 가장 작은 숫자~
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    tuple_ = tuple(map(int, input().split()))
    lst.append(tuple_)
lst.sort()
print(lst)


# start = []
# for i in range(len(lst)):
#     start.append(lst[i][0])

# print(start)
# idx = start.index(min(start))
# print(lst[idx][1])
# start.sort()
# print(start)
# # [0, 1, 2, 3, 3, 5, 5, 6, 8, 8, 12]
# for i in start:
#     if lst[idx][1] <= i:

#         # while(True):
#         #     if len(lst) == 0:
#         #         break
