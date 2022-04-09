# 1110 (성공)
# https://www.acmicpc.net/problem/1110
num = []
first_num = int(input())
input_ = first_num

while True:
    a = input_//10
    b = input_ % 10
    c = a+b

    if c < 10:
        input_ = 10*b + c
    elif c >= 10:
        input_ = 10*b + (c % 10)

    num.append(input_)

    if first_num == num[-1]:
        break

print(len(num))
