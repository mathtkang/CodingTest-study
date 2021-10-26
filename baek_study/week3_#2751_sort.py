# 수 정렬하기 2 (성공)
# https://www.acmicpc.net/problem/2751
# 참고 : https://assaeunji.github.io/python/2020-05-06-bj2751
'''
pypy3 이용
'''
n = int(input())
num = []

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)
