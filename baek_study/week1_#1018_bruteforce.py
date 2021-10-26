# 체스판 다시 칠하기 (다시)
# https://www.acmicpc.net/problem/1018
'''
[문제 접근 방식]
1. m*n 받는 리스트 생성
2. 색 비교(검은색 : 0, 흰색 : 1)

바깥 for문을 행(M)번 반복하고
그 안에 있는 내부 for문을 열(N)번 반복

행(M) : 라인 하나당 cnt++ 한 뒤에 넘겨주기
열(N) : 

다시 풀어보기
'''

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)


#
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                # (0, 0)(0, 2)(0, 4)(0, 6)...
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    elif original[i][j] != 'B':
                        index2 += 1
                # (0, 1)(0, 3)(0, 5)(0, 7)...
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    elif original[i][j] != 'W':
                        index2 += 1
        # 흑돌과 백돌중 조금 바꿔도 되는 돌을 계산하여 넣어준다.
        count.append(min(index1, index2))

print(min(count))
