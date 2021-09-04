'''
p.110 상하좌우
space_size만큼의 크기를 같는 정방행렬
첫 좌표가 1,1일 때 최종 좌표 구하기
'''
space_size = int(input())
direction = input().split()
x, y = 1, 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction_types = ["R", "D", "L", "U"]
# 움직이는 방향 리스트와 동일한 인덱스로 x, y 변화하는 값 인덱스

for d in direction:
    for i in range(len(direction_types)):
        if direction_types[i] == d:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > space_size or ny < 1 or ny > space_size:
        continue
        # 범위를 벗어날 경우 다시

    x, y = nx, ny

print(x,y)
