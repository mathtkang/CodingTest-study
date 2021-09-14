from collections import deque
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for i in range(N):
    num += K-1
    if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        num %= len(arr)

    answer.append(str(arr.pop(num)))

print("<", ", ".join(answer)[:], ">", sep='')


#####

n, k = map(int, input().split())

# 1부터 n까지의 덱 생성
dq = deque([i for i in range(1, n+1)])

result = []

# 덱의 원소가 사라질 때까지 반복
while dq:
    # k-1만큼의 덱의 맨 앞의 원소를 뒤로 저장 후 k번째의 원소를 result에 저장
    # 문자열로 저장하는 이유는 join를 사용하기 위해서
    for _ in range(k-1):
        dq.append(dq.popleft())
    result.append(str(dq.popleft()))

print("<", end="")
print(', '.join(result), end="")
print(">")
