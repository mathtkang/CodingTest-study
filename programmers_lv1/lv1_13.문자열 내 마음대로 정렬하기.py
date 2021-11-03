def solution(strings, n):
    answer = []

    lst = []
    for string in strings:
        lst.append(string[n]+string)  # 요기 아이디어!

    lst.sort()
    for i in lst:
        answer.append(i[1:])

    return answer
