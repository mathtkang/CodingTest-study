from collections import deque
'''
deque는 스택과 큐의 기능을 모두 가진 객체
출입구를 양쪽에 가지고 있다.

[deque가 가지고 있는 메서드]
.append(item) : item을 데크의 오른쪽 끝에 삽입
.appendleft(item): item을 데크의 왼쪽 끝에 삽입
.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가
'''
deq = deque()
# 이렇게 선언해주면 deq라는


a = deque([i for i in range(10)])  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# deque([[-1, -2], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.appendleft([-1, -2])


'''
https://dongdongfather.tistory.com/72
https://leonkong.cc/posts/python-deque.html
https://nero.devstory.co.kr/post/pl-python-collections-deque/
'''
