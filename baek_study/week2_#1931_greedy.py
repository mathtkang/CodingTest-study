# 회의실 배정 (완료)
# https://www.acmicpc.net/problem/1931
'''
[문제 이해]
하나의 회의실만 사용 가능한데, 최대한 많은 회의가 이루어질 수 있도록

[힌트]
(1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다. => 튜플형태

[문제 접근 방식]
리스트와 튜플 형식으로 저장
회의시간이 짧은 것, 
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    list_ = list(map(int, input().split()))
    lst.append(list_)
    # 같은 말
    # f, s = map(int, input().split())
    # lst.append([f, s])

# 끝나는 시간 x[1] 오름차순 정렬 -> 시작시간 x[0] 오름차순 정렬

lst.sort(key=lambda x: (x[1], x[0]))
# 같은말
# 시작 시간을 기준으로 정렬 후
# lst = sorted(lst, key = lambda x: x[0])
# 끝나는 시간을 기준으로 정렬
# lst = sorted(lst, key = lambda x: x[1])

cnt = 1
end_num = lst[0][1]

for i in range(1, len(lst)):
    if end_num <= lst[i][0]:
        end_num = lst[i][1]
        cnt += 1

print(cnt)
