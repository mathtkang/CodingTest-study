# [수학] 덧셈을 모르는 체셔
'''
[문제 접근 방식]

두 수는 10 이하 이기 때문에, 2자리수, 3자리 수, 4자리 수에 따라서 경우의 수가 나뉜다

1. 2자리 수인 경우, a와 b가 각각 1자리 임을 알 수 있다.
2. 3자리 수인 경우,
    1) 10* => 10 + *
    2) *10 => * + 10
3. 4자리 수인 경우 <=> 1010 => 10+10
'''
input = input()
N = str(input)
num = int(input)
if len(N) == 2:
    result = int(N[0]) + int(N[1])
elif len(N) == 3:
    if num <= 109:
        result = int(N[0] + N[1]) + int(N[2])
    else:
        result = int(N[0]) + int(N[1] + N[2])
elif num == 1010:
    result = 10+10

print(result)
