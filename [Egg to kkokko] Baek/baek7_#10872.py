# 팩토리얼
# https://www.acmicpc.net/problem/10872

# 1) math 모듈 이용
import sys
# import math
# mul = math.factorial(N)
# print(mul)

input = sys.stdin.readline

N = int(input())

# # 2) for문 이용
# result = 1
# for i in range(N, 0, -1):  # N에서 1까지 역순으로 숫자 생성
#     result *= i
# print(result)

# 3) 재귀함수 이용


def factorial(n):
    if n <= 1:  # 여기서 n == 1이라고 하면 런타임에러 발생 (이하라고 명시해줘야함)
        return 1
    else:
        return n*factorial(n-1)
        # 아직 실행되지 않은 채로 누적되어 있음
        # 마지막 1을 찍고 지금까지 누적된 함수 계산이 한번에 이루어짐


print(factorial(N))
