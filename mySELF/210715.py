# A, B = map(int, input().split())

# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")

# while True:
#     A, B = map(int, input().split(" "))
#     if A == null and B == null:
#         break
#     else:
#         print(A+B)

# # 값이 주어지지 않는 경우 try-except를 이용해서!!
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break


# # 1110
# num = []
# first_num = int(input())
# input_ = first_num

# while True:
#     a = input_//10
#     b = input_ % 10
#     c = a+b

#     if c < 10:
#         input_ = 10*b + c
#     elif c >= 10:
#         input_ = 10*b + (c % 10)

#     num.append(input_)

#     if first_num == num[-1]:
#         break

# print(len(num))
