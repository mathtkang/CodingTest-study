# 최소공배수

import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
        # a, b = b, a % b
    return a


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
