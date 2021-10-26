# 잃어버린 괄호 (다시)
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

lst = input().split("-")

sum_ = 0
in_sum = 0

for i in lst:
    if "+" in i:
        lst2 = []
        lst2 = i.split("+")
        lst2 = [int(j) for j in lst2]
        in_sum += sum(lst2)
    else:
        sum_ += int(i)

sum_ -= in_sum
print(sum_)


# 예주
arr = input().split("-")
# print(arr)

numbers = []

# 각 요소에 +가 있는거 더해주기
for i in arr:

    num = i.split("+")  # 덧셈을 해야하는 리스트를 따로 만듬
#     print(num)
    temp = 0
    for j in num:
        temp += int(j)
    numbers.append(temp)  # 덧셈을 한 요소를 새로운 리스트에 저장 # 여기있는 요소들을 빼주면 됨


answer = 0
# print(numbers)
for i in range(len(numbers)):
    if i == 0:
        answer += numbers[i]
    else:
        answer -= numbers[i]

print(answer)


# 상현
expression = input().split("-")
ans = 0
for i in expression[0].split("+"):
    ans += int(i)

for i in expression[1:]:
    for j in i.split("+"):
        ans -= int(j)

print(ans)
