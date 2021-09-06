'''
p.115 왕실의 나이트
8x8 좌표평면에서 이동할 때는 L자 형태로만 이동가능하다.(수평으로 2칸 + 수직으로 1칸 or 수직으로 2칸 + 수평으로 1칸)
행은 1~8, 열은 a~h까지로 설정되어있고 좌표를 벗어나지 않는 선에서 사용자가 위치를 입력하면 몇가지 방법으로 이동가능한지 횟수 반환

내 풀이) 이동하는 방법은 정해져 있기 때문에 이동 가능한 횟수로 구간을 나누어 확인
c3~f6 구간은 8가지,
c1~f2, c7~f8, a3~b6, g3~h6 : 4가지
b2,b7,g2,g7 : 4가지
a1,h2,a8,h8 : 2가지
나머지는 3가
'''
import time

row = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8
}
line = [1,2,3,4,5,6,7,8]

loc = input()

start = time.time()

loc_row = row[loc[0]]
loc_line = int(loc[1])

def find(x,y):
    if x >=3 and x <=6 and y >=3 and y <=6:
        return 8
    elif x >= 3 and x <=6 and y <= 2 and y >= 7:
        return 4
    elif x <=2 and x >= 7 and y <=3 and y <= 6:
        return 4
    elif x in [1,8] and y in [1,8]:
        return 2
    elif x in [2,7] and y in [2,7]:
        return 4
    else:
        return 3

print(find(loc_row, loc_line))

end = time.time()

print(end-start)        # 9.5367431640625e-05
