# [수학] 근거 없는 자신감
'''
https://velog.io/@aonee/k-s-listmapintinput.split
'''

import sys
input = sys.stdin.readline

N, *lst = list(map(int, input().split()))
# print(lst)

result = sum(lst)/N
# print(result)


# 평균을 넘는 학생 비율 (평균값 포함 안됨) 초과!!
p = 0

for i in range(N):
    if lst[i] > result:
        p += 1

processpoint = p*100/N

print("%0.3f%%" % processpoint)
