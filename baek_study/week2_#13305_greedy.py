# 주유소
# https://www.acmicpc.net/problem/13305
'''
[문제 이해]

[문제 접근 방식]
'''
N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])

print(sum)
