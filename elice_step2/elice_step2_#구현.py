# [구현] 직각삼각형
'''
https://www.acmicpc.net/problem/4153
'''
while True:
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    a.remove(max_num)
    if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
        print('rightangle')
    else:
        print('triangle')
