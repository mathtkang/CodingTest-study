# 덱 사용
import sys
from collections import deque

num = int(sys.stdin.readline())

deque = deque([i for i in range(1, num+1)])  # 1~n까지 덱 생성

while(len(deque) > 1):
    deque.popleft()  # 덱의 왼쪽 첫번째 원소 삭제
    deque.append(deque.popleft())  # 덱의 왼쪽 첫번째 원소를 맨 뒤에 붙임
    # move_num = deque.popleft()
    # deque.append(move_num)
print(deque[0])


# 큐 사용
N = int(sys.stdin.readline())
arr = [i for i in range(1, N+1)]  # n까지 리스트 생성
# 같은말 # list(range(1, N+1))

while len(arr) > 1:
    if len(arr) % 2:
        t = [arr[-1]]
        t.extend(arr[1::2])
        arr = t
    else:
        arr = arr[1::2]
print(arr[0])

while len(arr) > 1:
    arr.pop(0)
    temp = L.pop(0)
    arr.append(temp)
print(arr.pop(0))


# 규칙 찾아서 구현
input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break
