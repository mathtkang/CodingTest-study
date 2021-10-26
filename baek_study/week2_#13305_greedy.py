# 주유소 (다시)
# https://www.acmicpc.net/problem/13305
'''
[문제 이해]
첫째줄 : 마을의 갯수
둘째줄 : 각 마을 사이의 도로의 갯수 => 내가 채워야하는 리터(양)
셋째줄 : 마을에서 채울 수 있는 기름의 1리터 당 가격
처음에는 기름이 없음 -> 첫번째 마을에서는 무조건 결제해야 함
마지막 마을의 가격은 상관없음

[문제 접근 방식]
L과 W의 리스트 갯수는 W가 하나 더 많다
마지막 마을의 가격은 필요 없으니까 W의 마지막 원소를 제거
L과 W의 순서를 바꿔준다.

셋째줄의 마을에서 채울 수 있는 기름의 리터들을 비교해서 

'''

# 왼쪽 도시에서 오른쪽 도시로 가는 최소 비용 출력

# 첫번째 도시에서 무조건 사야함 -> 최소비용만 구매
# 제일 낮은 기름값일때 많이 사기
# 현재 도시 기름값이 다음도시 기름값보다 크면 두 도시 사이 거리만큼 사기
# 작다면 더 싼값이 있는 다음 도시까지 기름 사기


import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
W = list(map(int, input().split()))
# 마지막 원소 제거
W.pop()
# 뒤집어서 정렬
L.reverse()
W.reverse()

# print(N)
# print(L)
# print(W)

# 더 간단하게는?
re_L = []
for i in range(len(L)):
    sum_ = 0
    for j in range(i+1):
        sum_ += L[j]
    re_L.append(sum_)

print(re_L)  # [1, 4, 6]

# for i in L:
#     sum_ += i
#     L[i:]

# 타입에러 : i+1가 존재하지 않음 (그렇다고 i=1부터 하면 전체가 계수되지 않아서 값이 달라짐)
result = 0
for i in range(len(W)):
    if W[i] > W[i+1]:  # 4 > 2
        result += W[i+1]*re_L[i+1]
        if i+1 == len(W):
            break
    result += W[i]*L[i]

print(result)


# 예주

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0

current_price = price[0]

for i in range(0, len(price)-1):
    if current_price <= price[i]:  # 다음 도시가 더 비쌈
        answer = answer + (current_price * distance[i])
    else:
        current_price = price[i]
        answer = answer + (current_price * distance[i])

print(answer)


# another

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
price = length[0]*cost[0]
minCost = cost[0]

for i in range(1, len(length)):
    if minCost > cost[i]:
        minCost = cost[i]
    currentPrice = minCost * length[i]
    price += currentPrice

print(price)

# length가 0일 때에는 초기값으로 처리해주고
# for i in range(1,len(length))
# 이런식으로 처리하는 것이 일반적
