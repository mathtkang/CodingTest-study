def solution(s):
    idx = len(s)//2
    answer = ''
    if len(s) % 2 == 1:  # 홀수
        answer = s[idx]
    else:
        answer = s[idx-1] + s[idx]

    return answer
