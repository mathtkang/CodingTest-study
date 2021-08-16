# [수학] 숫자 나라 특허 전쟁
'''
[문제 접근 방식]

주어진 숫자 n보다 작은 수 
중에서 3과 5의 배수를 찾아서 
하나의 배열에 담고 
그 배열의 원소들의 총 합을 구해라
'''
num = int(input())  # 주어진 값이 하나니까
lst = []
sum = 0

for i in range(num):  # num-1까지
    if (i % 3 == 0) or (i % 5 == 0):
        lst.append(i)
        # print(i)

for i in range(len(lst)):
    sum += lst[i]

print(sum)
