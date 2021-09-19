# [수학] 앞면 뒷면
'''
[문제 접근 방식]
앞면을 0, 뒷면을 1이라고 하자
길이가 N인 리스트를 만들고 안의 값을 0(앞면이 보이도록)으로 초기화 한다

매개변수(p)의 배수에 해당하는 index를 list(index)로 호출, 이때 list(index)의 값이 0이면 1로, 1이면 0으로 바꾸는 함수를 만든다
for문을 통해서 1~N까지 함수를 호출하고 최종적인 list에서 뒷면(1)의 갯수를 카운트
'''

N = int(input())
lst = [0 for i in range(N)]  # 길이가 N, 각각의 값이 0으로 초기화 된 리스트
lst_idx = []  # 값을 바꿔줄 인덱스 담는 리스트

for i in range(1, N+1):
    for j in range(1, N+1):
        idx = i*j
        if idx <= N:
            lst_idx.append(idx)

# print(lst_idx)

# 인덱스에 따라서 값을 바꿔주자 (0<->1)
for i in lst_idx:
    if lst[i-1] == 0:
        lst[i-1] = 1
    elif lst[i-1] == 1:
        lst[i-1] = 0

# print(lst)

print(lst.count(1))


# for i in range(N):
#     change(i+1)

# def change(매개변수):
#     for i in range(1, N):
#         idx = p*(i+1)
#         if lst[idx] == 0:
#             lst[idx] = 1
#         elif lst[idx] == 1:
#             lst[idx] = 0
#     # if
#     pass
