# 나머지 (성공)
# https://www.acmicpc.net/problem/3052
import sys
input = sys.stdin.readline

# 나머지 담는 리스트
num_list = []

for i in range(10):
    num = int(input()) % 42
    num_list.append(num)

# num_list에서 중복 제거
# => 데이터 타입 : set->list
num_set = set(num_list)
num_list = list(num_set)

print(len(num_list))
