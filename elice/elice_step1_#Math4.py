# [수학] 바쁘다 바빠
'''
[문제 접근 방식]
초로 이루어진 모든 시간을 다 더한 후,
분,초로 변환해준다
'''
# global s
# s = int(input("초를 입력하시오."))

# def hms():
#     global s
#     hours = s // 3600
#     s = s - hours*3600
#     mu = s // 60
#     ss = s - mu*60
#     print(hours, '시간', mu, '분', ss, '초 입니다.')

# hms()

# m, s = divmod(seconds, 60)
# h, m = divmod(m, 60)


from datetime import timedelta
lst = []
for _ in range(4):
    num = int(input())
    lst.append(num)

sum_seconds = 0
for i in range(len(lst)):
    sum_seconds += lst[i]

print(datetime.timedelta(seconds=sum_seconds))
