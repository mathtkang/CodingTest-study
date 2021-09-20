# [수학] 앞면 뒷면
'''
[문제 접근 방식]
앞면을 0, 뒷면을 1이라고 하자
길이가 N인 리스트를 만들고 안의 값을 0(앞면이 보이도록)으로 초기화 한다

1부터 N까지 각각 배수에 해당하는 index를 list(index)로 호출, 이때 list(index)의 값이 0이면 1로, 1이면 0으로 바꾸는 로직을 만든다

=> 이렇게 하면 시간초과 발생

[또 다른 접근]
0에서 1로, 1에서 0으로 여러번 바꾸는게 아니라 어떤 수가 바뀌는지 찾고 해당하는 숫자만 count해준다

기존의 카드는 앞면(0)-> 이를 홀수번 뒤집어야 뒷면(1)이 된다.

(자신의 약수가 앞에서 존재하면 자신을 바꾸기 때문에 바뀌는 횟수가 홀수가 되기위해서는 약수의 갯수가 홀수여야 한다.)

약수의 갯수가 홀수인 수는 완전제곱수이므로,
따라서, 1부터 N까지 제곱수의 갯수 = 뒷면이 보이게되는 카드의 수
'''
N = int(input())

# sol1) 시간초과 발생
# lst = [0 for i in range(N)]  # 길이가 N, 각각의 값이 0으로 초기화 된 리스트
# lst_idx = []  # 값을 바꿔줄 인덱스 담는 리스트

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         idx = i*j
#         if idx <= N:
#             lst_idx.append(idx)

# # print(lst_idx)

# # 인덱스에 따라서 값을 바꿔주자 (0<->1)
# for i in lst_idx:
#     if lst[i-1] == 0:
#         lst[i-1] = 1
#     elif lst[i-1] == 1:
#         lst[i-1] = 0

# # print(lst)

# print(lst.count(1))


# sol2) 또 다른 접근방식
lst_ = []
for i in range(1, N//2+1):
    pow_ = i*i
    if pow_ <= N:
        lst_.append(pow_)

print(len(lst_))

# sol3) 제곱근을 이용해서 -> 주어진 수의 제곱근의 갯수
# print(int(N**0.5))
