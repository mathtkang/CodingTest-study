# 최댓값

import sys
input = sys.stdin.readline

num_lst = []

for i in range(9):
    num_lst.appned(int(input()))

# max함수 구현하면 런타임에러남
max = num_lst[0]
for i in num_lst:
    if max < i:
        max = i

# print(max)
# print(num_lst.index(max)+1)
print(max(num_list))
print(num_lst.index(max(num_lst))+1)
