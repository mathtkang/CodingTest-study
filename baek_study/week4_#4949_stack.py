# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
'''
[문제 이해]
괄호의 종류 : 소괄호("()"), 대괄호("[]")
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.

[문제 접근 방식]
.는 한줄 입력 종료
stack에 시작된 괄호를 저장해주고 
짝이 맞는 괄호가 오면 pop
짝이 맞지 않는 괄호가 오면 stack 리스트 그대로 둠
stack이 비어있으면 yes, 비어있지 않으면 no
'''
import sys
sys.stdin = open("input.txt")
# while input() != ".":

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    stack = []
    for i in string:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()  # del stack[-1]
            else:  # if not stack
                stack.append(']')
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')

    # 만약 while 문 밖에 input을 했으면 마지막 내부에 한번 더 선언을 해줘야 한다.
    # input = sys.stdin.readline().rstrip


'''
[알게된 것]
del stack[-1] VS stack.pop()
: pop()과 del은 지우고자 하는 리스트의 인덱스를 받아서 지우는 방식
차이 : pop()은 지워진 인덱스의 값을 반환, del은 반환하지 않음 -> 그래서 미미하게 del이 조금 더 빠름
remove()와 동일하게 pop()과 del은 특정 인덱스를 삭제한 후 다음 리스트를 재조정함
'''
