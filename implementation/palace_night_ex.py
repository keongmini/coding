'''
p.110 상하좌우 와 비슷한 유형의 풀이
'''

import time

input_data = input()

start = time.time()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord() : 문자의 유니코드 값을 반환해주는 함수
# a의 유니코드값을 기준으로 값비교하여 정수형으로 반환하기

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,2), (1,2), (-1,-2), (1,-2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)

end = time.time()

print(end-start)    # 0.0001430511474609375