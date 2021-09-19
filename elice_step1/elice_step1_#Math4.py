# [수학] 바쁘다 바빠
'''
[문제 접근 방식]
초로 이루어진 모든 시간을 다 더한 후,
분,초 로 변환해준다
'''
sum_ = 0
for _ in range(4):
    sum_ += int(input())

# print(sum_)

x = sum_//60
y = sum_ % 60

print(x)
print(y)
