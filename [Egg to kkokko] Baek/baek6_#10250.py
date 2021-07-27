# 10250 : ACM호텔
# https://www.acmicpc.net/problem/10250

people = int(input())
lst = []

for _ in range(people):
    H, W, N = map(int, input().split())
    Q = (N//H)+1  # 몫
    R = N % H  # 나머지
    room_num = R*100 + Q
    lst.append(room_num)

for i in range(len(lst)):
    print(lst[i])
