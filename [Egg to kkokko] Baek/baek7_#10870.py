# 피보나치 수 5
# https://www.acmicpc.net/problem/10870
import sys
input = sys.stdin.readline
N = int(input())


# for문 이용 : 런타임에러
def fibonacci_for(n):
    current = 0
    next_ = 1
    for _ in range(n):
        current = next_
        next_ = current + next_
    return current


print(fibonacci_for(N))


# 재귀함수 이용
def fibonacci_(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_(n-1)+fibonacci_(n-2)


print(fibonacci_(N))
