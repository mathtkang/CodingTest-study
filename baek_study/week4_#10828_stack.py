# 스택 (성공)
# https://www.acmicpc.net/problem/10828
'''
[문제 접근 방식]
스택을 리스트로 본다.
띄어쓰기를 기준으로 리스트로 받는다
각 명령어에 따라서 다르게 처리해준다
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
