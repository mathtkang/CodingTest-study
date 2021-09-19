# [수학] 도어락 비밀번호
'''
[문제 접근 방식]

주어진 숫자를 역순으로 되돌리는 것이기 때문에,
1) 코치님이 알려주신 방법? a[::-1] 을 사용해도 되고
2) for, list 를 이용해서 새로운 숫자를 만들어도 된다.

두개의 숫자가 주어지고
각각의 숫자를 뒤집은 다음, 합해준다
'''
a, b = map(str, input().split())

# print(a[::-1])
# print(b[::-1])

print(int(a[::-1]) + int(b[::-1]))
