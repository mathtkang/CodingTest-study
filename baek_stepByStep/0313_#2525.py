# 오븐 시계
# https://www.acmicpc.net/problem/2525
'''
[문제 접근 방식]
sol1) C를 60을 기준으로 두가지 경우의 수로 나눈다.
sol2) 60을 기준으로 몫과 나머지의 관점으로 본다.
'''

# sol1)
A, B = map(int, input().split())
C = int(input())

if C < 60:
    if B+C >= 60:
        A += 1
        B += C - 60
    else:
        B += C
else:  # C >= 60
    Q = C // 60
    R = C % 60
    A += Q
    B += R
    if B >= 60:
        A += 1
        B -= 60

if A >= 24:
    A -= 24

print(A, B)

# sol2)
H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)
