# 괄호
# https://www.acmicpc.net/problem/9012
'''
[문제 이해]
괄호 문자열(Parenthesis String, PS) : 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열
올바른 괄호 문자열(Valid PS, VPS) : 괄호의 모양이 바르게 구성된 문자열
기본 VPS : 한 쌍의 괄호 기호로 된 “( )” 문자열

[문제 접근 방식]
'('이 들어오면 stack에 append
')'이 들어오면 stack에서 '('를 pop
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    VPS = input()
    stack = []  # 리스트 생성시 : stack = list() 도 가능

    for ps in VPS:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break  # 예외적인 상황이니까 그 뒤로는 안따져봐도 됨
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

# 또 다른 풀이 : 직접 append, pop 하지 않고 숫자를 카운트

T = int(input())
for _ in range(T):
    VPS = input()  # 문자열이라 list안씌워도 됨
    sum = 0

    for ps in VPS:
        if ps == '(':
            sum += 1
        elif ps == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")
