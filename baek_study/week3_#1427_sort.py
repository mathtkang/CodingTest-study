# 소트인사이드
# https://www.acmicpc.net/problem/1427
import sys

'''
python : print(end = "", sep = "")
print()는 항상 개행이 포함되어있다.
개행을 하지 않게 하거나 각 출력값 사이에 내가 원하는 문구를 넣어줄 수 있다
'''
print("1-1칸", "1-2칸", "1-3칸", end="**end 입니다** \n")
# 1-1칸 1-2칸 1-3칸**end 입니다**  : 한 줄의 끝에
print("2-1칸", "2-2칸", "2-3칸", sep="**sep입니다**")
# 2-1칸**sep입니다**2-2칸**sep입니다**2-3칸  : 각 출력 값 사이에


sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

lst = list(map(int, str(N)))
# 같은말
# lst = []
# for i in N:
#     lst.append(int(i))

lst.sort(reverse=True)

for i in lst:
    print(i, end='')
