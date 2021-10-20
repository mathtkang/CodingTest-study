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
input = sys.stdin.readline
# while input() != ".":

while True:
    string = input()
    if string == '.':
        break

    stack = []
    for i in string:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()  # 맞으면 지워서 stack을 비워줌 0 = yes
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')

    input = sys.stdin.readline().rstrip


# arr = []

# while(True):
#     string = input()
#     if string == '.':  # .이 들어오면 입력 끝
#         break
#     arr.append(string)


# stack = []  # () 임시 저장공간

# for str in arr:
#     for element in str:

#         if element == "(" or element == "[":
#             stack.append(element)

#         if element == ")":

#             if not stack:  # 스택이 비어있는데 ) 들어오면 ㄴㄴ
#                 stack.append("end")

#             if stack[-1] == "(":  # 마지막거랑 짝이 맞을때만 삭제
#                 del stack[-1]
#             else:
#                 break

#         elif element == "]":
#             if not stack:
#                 stack.append("end")

#             if stack[-1] == "[":
#                 del stack[-1]
#             else:
#                 break

#     if stack:
#         print("NO")
#     else:
#         print("YES")
#     stack = []  # 스택 초기화
