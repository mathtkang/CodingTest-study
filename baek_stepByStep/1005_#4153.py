# 직각삼각형
# https://www.acmicpc.net/problem/4153
'''
[문제 접근 방식]
while문으로 0 0 0이 입력될 때까지 계속 한다
입력되는 값을 리스트로 넣어주고
(가장 큰 값)^2 = (나머지 값 1)^2 + (나머지 값 1)^2 : 직각 삼각형의 조건
인지 판단 해서 맞으면 right, 틀리면 wrong 반환
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

while(True):
    lst = list(map(int, input().split()))
    if lst == [0, 0, 0]:
        break
    # sol1) 내림차순으로 재배열 후 각각에 대해 비교
    lst.sort(reverse=True)
    a = lst[0]**2
    b = lst[1]**2
    c = lst[2]**2
    if a == b+c:
        print("right")
    else:
        print("wrong")
    # sol2) 가장 큰 요소를 추출 및 '삭제' 후 나머지 두 값으로 직각삼각형 조건 만족
