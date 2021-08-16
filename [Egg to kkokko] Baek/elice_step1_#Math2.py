# [수학] 김 박사의 비밀 데이터
'''
[문제 접근 방식]
한줄씩 입력되니까 map을 사용하기에는 무리가 있음!

'''
import sys
import math
input = sys.stdin.readline
N = int(input())  # 반복횟수 받음
# lst = list(map(int, input().split()))  #들어오는 변수를 각각 lst의 원소로 받음

lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

# print(lst)

sum = 0
for i in range(len(lst)):
    sum += lst[i]

# print(sum)

# sumTen = sum//10^10
# print(math.pow(10, 10))
# ten = math.pow(10, 9)
# sumTen = sum//ten

# -> 문자열로 접근
slicing = str(sum)
sumTen = slicing[0:10] #인덱스 0부터 10앞(9)까지  출력해라

print(sumTen)
