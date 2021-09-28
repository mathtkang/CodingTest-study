# 분해합
# https://www.acmicpc.net/problem/2231
'''
[문제 이해]
M의 분해합 : M과 M을 이루는 각 자리수의 합
(예. 256 = 245+2+4+5 / 216=198+1+9+8)

M의 분해합 = N
M = N의 생성자

자연수 N 주어질 때, 가장 작은 생성자는?

[문제 접근 방식]
N의 각 자릿수를 더할 때 문자열로 변환해서 더해주고 int화 해줌
'''
import sys
sys.stdin = open("input.txt")

N = int(input())
lst = []

for num in range(N, 0, -1):  # num = 245
    sumn = 0
    strN = str(num)  # "245"
    for i in strN:  # "2", "4", "5"
        sumn += int(i)  # sumn = 2+4+5
    result = num + sumn  # result = 245+2+4+5
    if result == N:
        lst.append(num)

# print(lst)
if not lst:
    print(0)
else:
    print(min(lst))


# 상현
N = int(input())

for creator in range(N):
    temp = sum(map(int, str(creator)))  # sum으로 바로 묶어줌
    totalSum = creator + temp
    if totalSum == N:
        print(creator)
        break
else:
    print(0)


# 예주
n = int(input())
answer = 0
for i in range(1, n+1, 1):
    num = list(map(int, str(i)))  # 하나씩 나눠서 리스트에 넣기
    sum_num = sum(num) + i
    if sum_num == n:
        answer = i
        break
print(answer)
