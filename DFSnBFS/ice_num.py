'''
p.149 음료수 얼려먹기
첫 줄에 NxM 크기의 얼음틀 설정
0은 구멍 뚫린 부분, 1은 칸막이가 있는 부분일때 구멍 뚫린 부분은 하나의 얼음이 된다.
이때 나오는 얼음의 개수는?
'''
N,M = map(int, input().split())

graph = [[j for j in map(int, input().split())] for i in range(N)]

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1,y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)