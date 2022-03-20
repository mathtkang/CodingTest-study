# 주사위 세개
# https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())

# nogada
result = 0

if a == b and b == c:
    result += 10000
    result += a*1000

elif a == b and b != c:
    result += 1000
    result += a*100

elif b == c and a != b:
    result += 1000
    result += b*100

elif a == c and b != c:
    result += 1000
    result += a*100

else:
    max_ = 0
    if a > b and a > c:
        max_ = a
    elif b > c:
        max_ = b
    else:
        max_ = c
    result += max_*100

print(result)

# short solution
if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a, b, c))
