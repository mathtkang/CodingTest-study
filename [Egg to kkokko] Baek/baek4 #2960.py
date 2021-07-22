# 에라토스테네스의 체
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
sieve_num = [True] * (N + 1)  # 체

for i in range(2, len(sieve_num) + 1):  # 2부터 체
    for j in range(i, N+1, i):
        if sieve_num[j] == True:
            sieve_num[j] = False
            cnt = cnt + 1

            if cnt == K:
                print(j)
                break
