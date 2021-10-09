# OX퀴즈
# https://www.acmicpc.net/problem/8958
'''
[문제 접근 방식]
'''
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
