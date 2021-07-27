# 10250 : ACM호텔
# https://www.acmicpc.net/problem/10250

people = int(input())
lst = []

for _ in range(people):
    H, W, N = map(int, input().split())
    Q = N//H  # 몫 -> 호
    R = N % H  # 나머지 -> 층

    if R == 0:
        # Q = N//H
        R = H  # 맨 꼭대기 층 수
    else:
        Q = N//H+1
        # R = N % H
    lst.append(R*100 + Q)

for i in range(len(lst)):
    print(lst[i])
