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

# string = 'aabbbcccc'
# print(Counter(string))
# #Counter({'c': 4, 'b': 3, 'a': 2})

# print(Counter(string).most_common(2))
# #[('c', 4), ('b', 3)]
# print(Counter(string).most_common(1))
# #[('c', 4)]
# print(Counter(string).most_common())
# # [('c', 4), ('b', 3), ('a', 2)] : 전체 요소 다 반환

'''(라이브러리 제외) 문제풀이 시작'''
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 산술평균 : math 라이브러리 사용 No. 내장 round() 메서드 사용하기!
print(round(sum(lst)/N))

# 중앙값
lst.sort()
print(lst[N//2])

# 최빈값
num3 = Counter(lst).most_common()  # 빈도의 value값을 추가해서 2차원 배열로 만들어줌
if len(lst) > 1 and num3[0][1] == num3[1][1]:
    print(num3[1][0])
else:
    print(num3[0][0])

# 범위(최댓값-최솟값)
print(max(lst)-min(lst))


# n = int(sys.stdin.readline())
# li = []
# for _ in range(n):
#     li.append(int(sys.stdin.readline()))

# # 산술평균 - 다 더해서 / n
# print(round(sum(li)/n))

# # 중앙값 - 오름차순 -> 중간값
# li.sort()
# print(li[n//2])

# # 최빈값 - 빈출
# cnt_li = Counter(li).most_common()
# if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
#     print(cnt_li[1][0])
# else:
#     print(cnt_li[0][0])

# # 범위 - 최댓값-최솟값
# print(max(li)-min(li))
