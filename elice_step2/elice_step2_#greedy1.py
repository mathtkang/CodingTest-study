# [그리디] 식기 세트 만들기
'''

'''

C, S, E = map(int, input().split())

if C//2 >= S:
    result = S
    remain = C % 2 + (C//2 - S)
else:
    result = C//2
    remain = C % 2 + (S - C//2)

if remain >= E:
    print(result)
else:
    print(result + (remain-E)//3)
