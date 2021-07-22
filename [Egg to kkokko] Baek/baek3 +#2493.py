# 탑
# stack이용
import math
import heapq
import stack
import sys
input = sys.stdin.readline


num = int(input())

arr = list(map(int, input().split()))
stack = []
ans = []

for i in range(num):
    while 1:
        if not stack:
            stack.append((i, arr[i]))
            ans.append(0)
            break
        if stack[-1][1] >= arr[i]:
            ans.append(stack[-1][0]+1)
            stack.append((i, arr[i]))
            break
        else:
            stack.pop()
print(*ans)


# heapq이용

N = int(input())
top = list(map(int, input().split()))
tmp = [(math.inf, 0)]
idx = 1
result = []

for i in range(N):
    if top[i] < tmp[0][0]:
        result.append(tmp[0][1])
        heapq.heappush(tmp, (top[1], idx))
    else:
        while True:
            heapq.heappop(tmp)
            if top[i] < tmp[0][0]:
                result.append(tmp[0][1])
                heapq.heappush(tmp, (top[1], idx))
                break
    idx += 1

print(*result)
