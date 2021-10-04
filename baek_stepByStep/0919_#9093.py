# 단어 뒤집기 (성공)
# https://www.acmicpc.net/problem/9093
'''
첫째줄 : 앞으로 몇개의 list가 입력될지
둘째줄~ : 한 줄이 하나의 리스트가 되도록
리스트 생성 후, 각 요소들을 [::-1]로 뒤집어준다. 이후 바로 출력
'''

N = int(input())
printf = ''

for i in range(N):
    lst = list(map(str, input().split(" ")))
    for j in range(len(lst)):
        string = lst[j]
        lst[j] = string[::-1]
        printf += lst[j] + ' '
    printf += '\n'
print(printf)
