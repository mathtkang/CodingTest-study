# 10818

# 입력받을 개수 정하기 -> 리스트의 개수 정하기
# 입력받은 것들 중에서 최소와 최대를 각각 출력

import sys
input = sys.stdin.readline
num = int(input())
num_lst = list(map(int, input().split()))  # 요기를 다르게해야할듯

# python 내장 함수 사용
print(min(num_lst))
print(max(num_lst))
print(min(num_lst), max(num_lst), end='')

# 직접 구현하기
min = num_lst[0]
max = num_lst[0]
for i in range(num):
    if min > num_lst[i]:
        min = num_lst[i]
    if max < num_lst[i]:
        max = num_lst[i]

print(min)
print(max)
