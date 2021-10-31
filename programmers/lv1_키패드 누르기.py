def cal_dist(num, now_l, now_r, pos, handed):
    X, Y = 0, 1
    dist_l = abs(pos[now_l][X] - pos[num][X]) + \
        abs(pos[now_l][Y] - pos[num][Y])
    dist_r = abs(pos[now_r][X] - pos[num][X]) + \
        abs(pos[now_r][Y] - pos[num][Y])
    # 거리가 같으면
    if dist_l == dist_r:
        return 'R' if handed == 'right' else 'L'
    return 'R' if dist_l > dist_r else 'L'


def solution(numbers, hand):
    # 왼손잡이인지 오른손잡이인지
    HANDED = hand
    # 번호 좌표화
    position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    # 왼쪽 숫자, 오른쪽 숫자
    left, right = set([1, 4, 7]), set([3, 6, 9])
    # 손 위치 초기화
    now_l, now_r = '*', '#'
    # solution
    result = ''
    for num in numbers:
        if num in left:  # 왼쪽 키라인
            result += 'L'
            now_l = num
        elif num in right:  # 오른쪽 키라인
            result += 'R'
            now_r = num
        else:  # 중간 키라인
            result += cal_dist(num, now_l, now_r, position, HANDED)
            if result[-1] == 'L':
                now_l = num
            else:
                now_r = num

    return result


'''경준님 풀이'''


def solution(numbers, hand):
    answer = ''
    L_tmp = (3, 0)
    R_tmp = (3, 2)
    for number in numbers:
        if number % 3 == 1:
            answer += 'L'
            L_tmp = ((number-1)//3, (number+2) % 3)
        elif number == 0:
            L_length = abs(L_tmp[0]-3)+abs(L_tmp[1]-1)
            R_length = abs(R_tmp[0]-3)+abs(R_tmp[1]-1)
            if L_length < R_length:
                answer += 'L'
                L_tmp = (3, 1)
            elif L_length > R_length:
                answer += 'R'
                R_tmp = (3, 1)
            else:
                if hand == 'right':
                    answer += 'R'
                    R_tmp = (3, 1)
                else:
                    answer += 'L'
                    L_tmp = (3, 1)
        elif number % 3 == 0:
            answer += 'R'
            R_tmp = ((number-1)//3, (number+2) % 3)
        else:
            x, y = (number-1)//3, (number+2) % 3
            L_length = abs(L_tmp[0]-x)+abs(L_tmp[1]-y)
            R_length = abs(R_tmp[0]-x)+abs(R_tmp[1]-y)
            if L_length < R_length:
                answer += 'L'
                L_tmp = (x, y)
            elif L_length > R_length:
                answer += 'R'
                R_tmp = (x, y)
            else:
                if hand == 'right':
                    answer += 'R'
                    R_tmp = (x, y)
                else:
                    answer += 'L'
                    L_tmp = (x, y)

    return answer
