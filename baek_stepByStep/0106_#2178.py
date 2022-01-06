# 미로 탐색
# https://www.acmicpc.net/problem/2178
'''
bfs를 이용한 문제

'''
# 엘리스 문제 풀이
import queue  # queue 모듈의 Queue 클래스를 사용하는 것
import sys
sys.setrecursionlimit(100000)


direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y, n, m, pMap, queue, visited):
    while queue:  # 큐가 비지 않는 동안
        del queue[0]

        # 상하좌우 탐색
        for i in direction:
            # nx, ny : 변경하기 위한 좌표
            nx = x + i[0]
            ny = y + i[1]

            # 인덱스를 초과하지 않으며, 경로가 존재하고, 방문하지 않은 지점일 경우
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] == True:
                continue
            elif visited[nx][ny] == False:
                if pMap[nx][nx] == 1:
                    queue.append([nx, ny])  # 4방향중 visited가 1이 들어간 곳에만 큐 추가
                    visited[nx][ny] = True
                    pMap[nx][ny] = pMap[x][y] + 1

    return pMap[n-1][m-1]


def maze(n, m, pMap):
    '''
    미로를 탈출하기 위해 이동해야 하는 최소 칸 수를 반환해야 합니다.
    '''
    queue = [[0, 0]]
    # 방문한 노드 거르기 위한 리스트
    visited = [[False for i in range(m)] for j in range(n)]

    # 출발점
    visited[0][0] = 1
    x, y = queue[0][0], queue[0][1]

    result = bfs(x, y, n, m, pMap, queue, visited)

    return result
