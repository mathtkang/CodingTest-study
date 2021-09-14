# 평균
import sys
input = sys.stdin.readline

# subject_num = int(input())
score = list(map(int, input().split()))
print(score)

M = max(score)

new_score = []
for i in range(len(score)):
    new_score.append(score[i]/M*100)
print(new_score)

avg = sum(new_score, 0.0)/len(new_score)
print(avg)
