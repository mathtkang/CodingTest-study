# [문자열] 마법 맷돌
'''
첫번째 줄에서 받은 입력값을 반복해서 출력하는 문자열 과
두번째 줄에서 받은 입력값을 반복해서 출력하는 문자열 이 같다면 1, 다르면 0 반환

각각의 결과를 담는 문자열이 따로 존재
'''

# import sys
# input = sys.stdin.readline
s = str(input())
t = str(input())

s_result = s*50
t_result = t*50

# print(s)
# print(t)

# print(s_result)
# print(t_result)

if s_result[:50] == t_result[:50]:
    print("1")
else:
    print("0")
