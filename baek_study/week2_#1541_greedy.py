# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
'''
[문제 이해]
괄호를 내가 넣고 싶은 곳에 넣어서 가장 최솟값으로 만든다
55-50+40 -> 55-(50+40) = 55-90 = -35
두 개 이상의 연산자는 나타나지 않음 -> 연산자는 2개가 최대

[문제 접근 방식]
연산자 2개의 경우의 수 : ++ / +- / -+ / --
+끼리 다 먼저 더하고 -끼리 해준다
연산자를 기준으로 input,list를 받는다.
'''
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
# input()으로 받는 값의 첫번째 요소가 +,-인지 확인 후 아래의 로직 실행
input_string = str(input())
print(input_string)


if input_string[0] == "-":  # 만약 -로 시작하면
    sum_
    pass


def func(input_, sum_):
    lst = list(map(str, input_.split("-")))
    lst.insert(0, '0')
    print(lst)

    sum_ = 0
    in_sum = 0
    for i in lst:  # ['55', '50+40', '30+20']
        if "+" in i:
            lst2 = []
            lst2 = i.split("+")  # ['50', '40']
            # lst2 = list(map(int, lst2))
            # 리스트 내부 요소 형변환 string->int # [50, 40]
            lst2 = [int(j) for j in lst2]
            print(lst2)
            print(sum(lst2))  # 90
            in_sum += sum(lst2)
            print(in_sum)
        else:
            sum_ += int(i)

            # print(in_sum)
    sum_ -= in_sum
    print(sum_)
