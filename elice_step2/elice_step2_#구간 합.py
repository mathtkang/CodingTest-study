# [구간 합] 재벌의 쇼핑
'''
총 상품의 갯수 : N, 쇼핑의 최소금액 : S
'''

N, S = map(int, input().split())
input_lst = list(map(int, input().split()))
input_lst.sort(reverse=True)

cnt = 0
num = S


def func(num, input_lst):
    global cnt
    # print(cnt)
    # print(num)
    # print(input_lst)
    for i in input_lst:  # [10, 9, 8, 7, 5, 5, 4, 3, 2, 1]
        if i == num:
            cnt += 1
            num -= i  # num = num - i
            input_lst.remove(i)
    # return func(num, input_lst)


for num in range(S, 0, -1):
    print(num)  # 15, 14, 13, ..., 1
    func(S, input_lst)

print(cnt)


# max_n = max(lst)
# # print(max_n)

# cnt = 0

# for _ in range(len(lst)):
#     if S-max_n >= 0: #15-10
#         cnt += 1
#         lst.remove(max_n)
#         S -= max_n
#         max_n = max(lst)
#         print(max_n)

#     else:
#         break
# print(cnt)
