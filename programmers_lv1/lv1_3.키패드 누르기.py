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


def solution(numbers, hand):
    ret = ""
    l_x, l_y = 0, 0
    r_x, r_y = 2, 0

    d_x, d_y = -1, -1

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            ret += ("L")
            if i == 1:
                l_x, l_y = 0, 3
            elif i == 4:
                l_x, l_y = 0, 2
            elif i == 7:
                l_x, l_y = 0, 1

        elif i == 3 or i == 6 or i == 9:
            ret += ("R")
            if i == 3:
                r_x, r_y = 2, 3
            elif i == 6:
                r_x, r_y = 2, 2
            elif i == 9:
                r_x, r_y = 2, 1

        else:
            if i == 2:
                d_x, d_y = 1, 3
            elif i == 5:
                d_x, d_y = 1, 2
            elif i == 8:
                d_x, d_y = 1, 1
            elif i == 0:
                d_x, d_y = 1, 0

            if (abs((d_x - l_x)) + abs((d_y - l_y))) == (abs((d_x - r_x)) + abs((d_y - r_y))):
                if hand == "left":
                    ret += ("L")
                    print(f"지금 숫자: {i}, 왼손 위치: {l_x, l_y}, 오른손 위치: {r_x, r_y}")
                    if i == 2:
                        l_x, l_y = 1, 3
                    elif i == 5:
                        l_x, l_y = 1, 2
                    elif i == 8:
                        l_x, l_y = 1, 1
                    elif i == 0:
                        l_x, l_y = 1, 0

                elif hand == "right":
                    ret += ("R")
                    print(f"지금 숫자: {i}, 왼손 위치: {l_x, l_y}, 오른손 위치: {r_x, r_y}")
                    if i == 2:
                        r_x, r_y = 1, 3
                    elif i == 5:
                        r_x, r_y = 1, 2ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
                    elif i == 8:
                        r_x, r_y = 1, 1
                    elif i == 0:
                        r_x, r_y = 1, 0

            elif (abs((d_x - l_x)) + abs((d_y - l_y))) > (abs((d_x - r_x)) + abs((d_y - r_y))):
                ret += ("R")
                print(f"지금 숫자: {i}, 왼손 위치: {l_x, l_y}, 오른손 위치: {r_x, r_y}")
                if i == 2:
                    r_x, r_y = 1, 3
                elif i == 5:
                    r_x, r_y = 1, 2
                elif i == 8:
                    r_x, r_y = 1, 1
                elif i == 0:
                    r_x, r_y = 1, 0

            elif (abs((d_x - l_x)) + abs((d_y - l_y))) < (abs((d_x - r_x)) + abs((d_y - r_y))):
                ret += ("L")
                print(f"지금 숫자: {i}, 왼손 위치: {l_x, l_y}, 오른손 위치: {r_x, r_y}")
                if i == 2:
                    l_x, l_y = 1, 3
                elif i == 5:
                    l_x, l_y = 1, 2
                elif i == 8:
                    l_x, l_y = 1, 1
                elif i == 0:
                    l_x, l_y = 1, 0
    return ret
