# [그리디] 잔돈 가득한 세상
'''

'''
N = int(input())
exchange = 10000-N

result = 0
for i in range(4, -1, -1):
    val = exchange // pow(10, i)
    result += val
    exchange -= val*pow(10, i)

print(result)
