import sys
input = sys.stdin.readline
a, b = map(int, input().split())

# 최대공약수


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        # a = b
        # b = a % b  # r
    return a

# 최소공배수


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))


###
A, B = map(int, input().split())
a, b = A, B
while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)
# lcm
print(A*B//a)
