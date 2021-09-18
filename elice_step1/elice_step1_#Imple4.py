# [구현] 생수통
'''
1~3줄 : 물통 가격
4~5줄 : 뚜껑 가격
물통 가격 중 가장 작은 값을 하나의 변수에 저장
뚜껑 가격 중 가장 작은 값을 또 다른 변수에 저장
두 변수 값을 더한 다음 마지막으로 10원 더해준 값이 생수통 한 개 가격의 최솟값
'''
# 여러줄에 걸쳐서 입력받기(line by line)
# : L,A,B,C,D = [int(input()) for _ in range(5)]

bottle = list(int(input()) for _ in range(3))
lid = list(int(input()) for _ in range(2))

min_bottle = min(bottle)
min_lid = min(lid)

print(min_bottle + min_lid + 10)
