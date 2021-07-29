# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729


import sys
sys.setrecursionlimit(10**7)

num = int(input())
print(2**num-1)


def hanoi(n, p1, p2, p3):
    # 원판이 하나일 때 이동은 p1 -> p3
    if n == 1:
        print(p1, p3)
    # 원판이 두개이상일때
    else:
        hanoi(n-1, p1, p3, p2)  # ex)원판이 두개인 경우 출력은 print(p1 p2)
        print(p1, p3)  # print (p1, p3)
        hanoi(n-1, p2, p1, p3)  # print(p2 p3)


hanoi(num, 1, 2, 3)

# 원판이 3개일때
'''
else 문으로 들어가면
1. hanoi(3-1, p1, p3, p2) 재귀
   hanoi(2, p1, p3, p2) -> hanoi(1, p1, p2, p3)=print(p1, p3) -> print(p1, p2)
    -> hanoi(1, p3, p1, p2)=print(p3, p2)

2. print(p1, p3)

3. hanoi(3-1, p2, p1, p3) 재귀
   hanoi(2, p2, p1 ,p3) -> hanoi(1, p2, p3, p1)=print(p2, p1) -> print(p2, p3)
     -> hanoi(1, p1, p2, p3)=print(p1, p3)


종합 순서
(p1 p3) -> (p1 p2) -> (p3 p2) -> (p1 p3) -> (p2, p1) -> (p2, p3) -> (p1, p3)
'''
