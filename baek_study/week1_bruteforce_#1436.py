# 영화감독 숌
# https://www.acmicpc.net/problem/1436
'''
[문제 접근 방식]
1부터 10,000까지의 숫자 중 '666'이 연속으로 들어가는 숫자를 리스트에 넣는다
입력된 번호를 index로 보고 해당하는 리스트값(n번째 영화 제목)을 출력
'''
import sys
sys.stdin = open("input.txt")

idx = int(input())
movie_name = [0]

for num in range(666, 10001):
    if "666" in str(num):
        movie_name.append(num)

print(movie_name)

print(movie_name[idx])
