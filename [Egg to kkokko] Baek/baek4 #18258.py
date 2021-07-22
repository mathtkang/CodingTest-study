# 큐2
from collections import deque
import sys
input = sys.stdin.readline

# 큐, 배열 이용 (덱 사용 안함)
n = int(input())
queue = []
cnt = 0

for _ in range(n):
    c = input().split()

    if c[0] == "push":
        queue.append(c[1])

    elif c[0] == 'pop':
        if len(queue) > cnt:
            print(queue[cnt])
            cnt += 1
        else:  # 큐가 비어있음
            print(-1)

    elif c[0] == 'size':
        print(len(queue)-cnt)

    elif c[0] == 'empty':
        if len(queue) == cnt:  # 큐가 비어있을 때
            print(1)
            cnt = 0  # 리셋 해주는거임?
            queue = []
        else:
            print(0)

    elif c[0] == 'front':
        if len(queue) > cnt:
            print(queue[cnt])
        else:
            print(-1)

    elif c[0] == 'back':
        if len(queue) > cnt:
            print(queue[-1])
        else:
            print(-1)


# deque 사용

n = int(input())
q = deque([])

for _ in range(n):
    s = input().split()

    if s[0] == 'push':
        q.append(s[1])

    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif s[0] == 'size':
        print(len(q))

    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
