# 파이썬 :  힙>최소힙 밖에 없다 : 최대힙을 구하고 싶으면 직접 구현해야함

import heapq
import sys
input = sys.stdin.readline

numbers = int(input())

heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))  # 절댓값 함수 : abs()
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)


######

N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x != 0:
        if x < 0:
            heapq.heappush(queue, (-x, 'minus'))
        else:
            heapq.heappush(queue, (x, 'plus'))
    else:
        if queue:
            value, status = heapq.heappop(queue)
            print(value if status == 'plus' else -value)
        else:
            print(0)


# 다른 풀이
N = int(input())
arr = []

for _ in range(N):
    val = int(input())

    if val == 0:
        if len(arr) == 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, val)

# 최소힙 구하기
arr = [1, 4, 2, 7, 5, 3, 3, 7, 8, 9]
heapq.heappush(arr, 0)
print(heapq.heappop(arr))
