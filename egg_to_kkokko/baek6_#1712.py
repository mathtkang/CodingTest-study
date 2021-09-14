# 손익분기점
# https://www.acmicpc.net/problem/1712

'''
설명
A : 고정비용
B : 가변비용
C : 판매비용
판매량 : n (우리가 반환해야하는 값)
총 비용(고정비용+가변비용) < 총 수입(판매비용)
=> A + nB < nC 가 되는 n의 값을 구하라
'''

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
if B >= C:
    print(-1)

# n = 1
# while True:
#     if A+n*B < n*C:
#         break
#     n += 1
# print(n)

print(A//(C-B) + 1)

# gross_income  # 총 수입(판매비용)
# total_cost  # 총 비용(고정비용+가변비용)
