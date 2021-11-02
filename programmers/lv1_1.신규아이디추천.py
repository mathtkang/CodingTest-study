'''김병철 코치님 풀이'''


def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join([c for c in new_id if c.islower()
                      or c.isdigit() or c in ['-', '_', '.']])

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')
    # if new_id:  # 비어있으면 false (len 안써도 됨)
    new_id = new_id if new_id else "a"
    new_id = new_id[:15].strip('.')

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


'''스갱 풀이'''


def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계 -sol1
    for i in new_id:
        if i == '-' or i == '_' or i == '.':
            continue
        else:
            new_id = new_id.replace(i, '')
    # 이렇게 하면 틀리는 이유..?

    # 2단계 -sol2
    answer = ''
    for i in new_id:
        # .isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.
        if i.isalnum() or i in '-_.':
            answer += i
    new_id = answer

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    # strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거 (한쪽만 제거는 아니다!)
    new_id = new_id.strip('.')
    # 5단계
    if new_id == '':
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]  # 마지막 오른쪽 '.'를 없애기
            # new_id = new_id.rstrip('.') #왜 이건 안되징

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


'''
#정규식
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    
'''
