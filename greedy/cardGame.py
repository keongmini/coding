'''
p.96 숫자 카드 게임
n x m 행렬로 놓여있는 카드, 각 행마다 행에 놓여있는 카드 중 가장 작은 값들을 선택 -> 그 중 가장 큰 값을 출력
n : 행, m : 열
* time 모듈을 이용하여 코드 진행 시간을 측정하려 했으나 코드 입력하는 시간까지 측정되어 정확한 시간 측정 불가
'''

'''
>> 1. 내 풀이(효율X) <<
import time

n, m = map(int, input().split())

numbers = []
minNum = []

start_time = time.time()

for i in range(n):
    mList = list(map(int, input().split()))
    numbers.append(mList)
    mList.sort()
    minNum.append(mList[0])

minNum.sort()
print(minNum[-1])

end_time = time.time()
print(end_time - start_time)    # 0.30493593215942383
'''

# >> 내 풀이(효율 고려, 책의 풀이와 유사) <<
import time

n, m = map(int, input().split())

minNum = 0

start_time = time.time()

for i in range(n):
    mList = list(map(int, input().split()))
    num = min(mList)
    if minNum < num:
        minNum = num

print(minNum)

end_time = time.time()
print(end_time - start_time)    # 0.19670701026916504