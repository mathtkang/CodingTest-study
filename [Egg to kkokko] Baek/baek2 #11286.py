import sys
import heapq
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


input = sys.stdin.readline

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
