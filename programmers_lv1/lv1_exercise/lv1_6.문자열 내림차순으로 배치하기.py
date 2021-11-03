def solution(s):
    answer = ''
    print(s)
    lst = sorted(s, reverse=True)  # 문자열 -> 리스트화
    print(lst)
    answer = "".join(lst)
    return answer
