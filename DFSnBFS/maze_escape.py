'''
p. 152 미로 탈출
N x M 크기의 미로에 있고 첫 위치는 (1,1)
0은 괴물이 존재, 1은 괴물이 없음
괴물이 없는 곳을 몇번 지나야 탈출할 수 있는지 횟수를 반환하기
'''

from collections import deque

N, M = map(int, input().split())

graph = [[j for j in map(int, input().split())] for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()       # 데크(queue) 안이 빌 때까지 반

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 모두 탐색(for반복문)

            # 배열의 범위를 벗어났을 때
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 괴물이 있는 곳
            if graph[nx][ny] == 0:
                continue

            # 괴물이 없는 곳
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                # 탐색해야하는 지점을 모두 넣어줌

    return graph[N-1][M-1]      # 탐색을 하면서 1씩 더해주기 때문에 마지막 탐색하는 지점의 값을 반환해주면 그게 탐색의 횟수가 됨

print(bfs(0,0))
