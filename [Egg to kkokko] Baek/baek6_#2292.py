# 벌집
# https://www.acmicpc.net/problem/2292
import sys
input = sys.stdin.readline

standard = 1
interval = 0

N = int(input())
if N == 1:
    interval = 0
else:
    i = 1
    while True:
        # print(N, i)
        standard += 6*i
        if N <= standard:
            interval = i
            break
        i += 1

print(interval + 1)


# -- other idea
# num = N-2
# n = 1
# div = num % 6
# for i in range(1,):
#     if num % (6*i) == i-1:
#         interval = i

#     if div == 0:
#         interval = 1
#     elif div == 1 or div == 2:
#         interval = 2
#     elif div == 3 or div == 4 or div == 5:
#         interval = 3


# -- another solution
# n = int(input())
# cnt = 1
# cnt_six = 6
# count = 1
# while n > cnt:
#     count += 1
#     cnt += cnt_six
#     cnt_six += 6
# print(count)
