# 블랙잭
# https://www.acmicpc.net/problem/2798
'''
[문제 접근 방식]
N개중 3개를 순서없이 뽑고, 그 3개의 값의 합들 중 M을 넘지않는 최대값을 반환
참고) https://duwjdtn11.tistory.com/297
'''

from itertools import combinations
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

list_combi = list(combinations(card_list, 3))

result = []

for i in list_combi:
    combi_sum = sum(i)
    if combi_sum <= M:
        result.append(combi_sum)

print(max(result))
