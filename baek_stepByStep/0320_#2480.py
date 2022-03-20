# 주사위 세개
# https://www.acmicpc.net/problem/2480
'''
[문제 접근 방식]
'''
a, b, c = map(int, input().split())
result = 0

if a == b and b == c:
    result += 10000
    result += a*1000

elif a == b and b != c:
    result += 1000
    result += a*100

elif b == c and a != b:
    result += 1000
    result += b*100

elif a == c and b != c:
    result += 1000
    result += a*100

else:
    if a > b and a > c:
