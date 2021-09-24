# [수학] 산수 왕 체셔
'''
(a의 b제곱)/c
걸리는 시간 : pow(a,b) == a**b
'''

a, b, c = map(int, input().split())
# print((a**b)%c)
print(pow(a, b) % c)
