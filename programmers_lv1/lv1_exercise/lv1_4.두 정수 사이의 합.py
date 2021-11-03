def solution(a, b):
    answer = 0

    if a > b:
        temp = a
        a = b
        b = temp
        # a, b = b, a

    for i in range(a, b+1):
        answer += i

    return answer
