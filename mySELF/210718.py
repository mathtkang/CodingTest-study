# 10818

# 입력받을 개수 정하기 -> 리스트의 개수 정하기
# 입력받은 것들 중에서 최소와 최대를 각각 출력

import sys
input = sys.stdin.readline
num = int(input())
lst = list(map(int, input().split()))  # 요기를 다르게해야할듯


print(num)
print(lst)


# min = lst[0]
# max = lst[0]
# for i in range(num):
#     if min > lst[i]:
#         min = lst[i]
#     if max < lst[i]:
#         max = lst[i]

print(min(lst))
print(max(lst))
