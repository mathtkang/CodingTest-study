# [DFS] 숫자 장식
'''

'''


def dfs(lst, M, tmp):
    if len(tmp) == M:
        return print(*tmp)

    for i in range(len(lst)):
        tmp.append(lst[i])
        dfs(lst, M, tmp)
        tmp.pop()


N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]
