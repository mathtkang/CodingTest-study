# 통계학
# https://www.acmicpc.net/problem/2108
'''
최빈값의 count를 위해서 collections.Counter(내장함수) 사용
이 함수는 dictionary 형태로 반환해준다.
Counter()의 메서드 중에서 .most_common(n)는 빈도가 높은 순서로 n개 반환
'''
from collections import Counter
import sys
import math

string = 'aabbbcccc'
print(Counter(string))
#Counter({'c': 4, 'b': 3, 'a': 2})

print(Counter(string).most_common(2))
#[('c', 4), ('b', 3)]
print(Counter(string).most_common(1))
#[('c', 4)]
print(Counter(string).most_common())
# [('c', 4), ('b', 3), ('a', 2)] : 전체 요소 다 반환

'''(라이브러리 제외) 문제풀이 시작'''
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 산술평균
num1 = math.floor(sum(lst)/N)
print(num1)

# 중앙값
idx = N//2
lst.sort()
num2 = lst[idx]
print(num2)

# 최빈값
num3 = Counter(lst).most_common()  # 빈도의 value값을 추가해서 2차원 배열로 만들어줌
if len(lst) > 1:
    if num3[0][1] == num3[1][1]:
        print(num3[1][0])
    else:
        print(num3[0][0])
else:
    print(num3[0][0])

# 범위(최댓값-최솟값)
num4 = lst[N-1] - lst[0]
print(num4)
