# [구현] 도도새의 업무일지
N = int(input())
_list = list(map(int, input().split()))

tmp = _list[0]

for i in range(1, len(_list)):
    _list[i] = _list[i]*(i+1) - tmp
    tmp += _list[i]

print(*_list)
