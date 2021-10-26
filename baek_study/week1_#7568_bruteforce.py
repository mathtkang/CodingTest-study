# 덩치 (완료)
# https://www.acmicpc.net/problem/7568
'''
[문제 접근 방식]
2차원 배열로 받아서 같은 열끼리 비교
arr2 = [
    [wA(0,0), hA(0,1)],
    [wB(1,0), hB(1,1)],
    [wC(2,0), hC(2,1)],
    [wD(3,0), hD(3,1)],
    [wE(4,0), hE(4,1)]
]
arr2[i][0] > arr2[j][0] && arr2[i][1] > arr2[j][1]
rank_list 로 비교하면 될 것 같은데!
'''
import sys
sys.stdin = open("input.txt")
# input = sys.stdin.readline

# sol1)
N = int(input())
arr2 = [list(map(int, input().split())) for _ in range(N)]
cnt_list = [1 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr2[i][0] < arr2[j][0] and arr2[i][1] < arr2[j][1]:
            # print(arr2[i][0], arr2[i][1])
            cnt_list[i] += 1

print(*cnt_list)  # list  ->string

# sol2)
# people = []
# for i in range(n):
#     people.append(input().split())


# for i in range(n):
#     grade = 1
#     for j in range(n):
#         if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
#             grade += 1
#     print(grade, end=" ")  # 배열로 안하고 하나씩 출력해줌
