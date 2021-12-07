import math

# 조건
time = 100
gold = 200
upgrade = [[0, 5], [1500, 3], [3000, 1]]


# 함수 안에 함수를 만들까?
def cnt():

    return answer


for i in upgrade:
    print(i)
    for j, w in i:
        print(j)


upgrade_cnt = 0
# 업그레이드 할때마다 1씩 증가

# 내가 가지고 있는 금액
money


업그레이드를 한번도 하지 않은 경우: 레벨 1
level = 0
money = 0
# 광석개수 = 제한시간//걸리는시간 : 100
seok = time//upgrade[level][1]
money += seok*200  # 최종 내돈 = 기존의 내 돈 + (광석개수*200원)

업그레이드를 한번 한 경우: 레벨 1 -> 2 (0 -> 1)
level = 0
money = 0

# 업그레이드를 위해서는 1500원이 필요하다
# 필요한 광석의 갯수 = 반올림(필요한 금액//200) #math.ceil(3.14) #결과는 4
# 소모한 시간 = 필요한 광석의 갯수(8) * 5초
time -= math.ceil(upgrade[level+1][0]//200)*upgrade[level][1]

# 얻은 돈 = math.ceil(upgrade[level+1][0]//200)*200원
money = math.ceil(upgrade[level+1][0]//200)*200

level += 1
# 내가 가지고 있는 금액에서 업그레이드 비용를 빼준다.
# 나의 돈 -= 업그레이드 비용
money -= upgrade[level][0]
# 광석개수 = 남은 제한시간//걸리는시간
seok = time//upgrade[level][1]
money += seok*200  # 최종 내돈 = 기존의 내 돈 + (광석개수*200원)


answer = []
# answer에서 가장 값이 큰 수를 반환
