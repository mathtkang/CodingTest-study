# [greedy] 식기 세트 만들기
'''

'''

C, S, E = map(int, input().split())

if C//2 >= S:
    result = S
    remain = C % 2 + (C//2 - S)
