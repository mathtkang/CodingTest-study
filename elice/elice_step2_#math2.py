# [수학] 피보나치 K번째 수는?
'''
피보나치 수열을 담고 있는 함수(배열x) 생성
'''
K = int(input())


def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr


print(fib(K))


# def fibo(n):
#     return fibo(n-1) + fibo(n-2) if n >= 2 else n

# for n in range(1, 11):
#     print(n, fibo(n))
