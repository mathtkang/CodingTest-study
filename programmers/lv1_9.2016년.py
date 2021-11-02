def solution(a, b):
    num = 0
    answer = ''
    lst = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    if a == 1:
        num = b
    elif a == 2:
        num = 31 + b

    elif a == 3:
        num = 31 + 29 + b

    elif a == 4:
        num = 31 + 29 + 31 + b

    elif a == 5:
        num = 31 + 29 + 31 + 30 + b

    elif a == 6:
        num = 31 + 29 + 31 + 30 + 31 + b

    elif a == 7:
        num = 31 + 29 + 31 + 30 + 31 + 30 + b

    elif a == 8:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + b

    elif a == 9:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + b

    elif a == 10:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + b

    elif a == 11:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + b

    elif a == 12:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + b

    for i in range(7):
        if num % 7 == i:
            answer = lst[i]

    return answer
