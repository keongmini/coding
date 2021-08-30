'''
p.92 큰 수의 법칙
주어진 리스트 내 숫자를 maxNum번 더해서 가장 큰 수를 만들기, 이때 한 숫자는 minNum번까지만 반복가능
num : 리스트 크기
'''


import time

num, maxNum, minNum = map(int, input().split())

numList = list(map(int, input().split()))

start_time = time.time()

numList.sort()

# firstNum = numList[-1]
# secondNum = numList[-2]

# 위 방법 대신 아래와 같이 작성하는 이유 : 리스트의 크기가 num이기 때문에 num을 넘어가는 숫자는 제외하기 위해
firstNum = numList[num-1]
secondNum = numList[num-2]
result = 0

'''
>> 내 풀이 << 
cnt = 0
plusCnt = 1

while True:
    if cnt == maxNum:
        break

    result += firstNum

    if plusCnt % minNum == 0 :
        result += secondNum
        cnt += 1

    plusCnt += 1

    cnt += 1

end_time = time.time()
print(result)   # 46
print(end_time - start_time)    # 2.0265579223632812e-05
'''

'''
1. 책의 첫번째 풀이 : 반복하는 숫자가 커진다면 시간 초과가 발생할 가능성이 높음
while True:
    for i in range(minNum):
        if maxNum == 0:
            break
        result += firstNum
        maxNum -= 1

    if maxNum == 0:
        break
    result += secondNum
    maxNum -= 1

end_time = time.time()
print(result)
print(end_time - start_time)    # 3.0994415283203125e-05
'''

'''
2. 책의 두번째 풀이 : 효율적 풀이
가장 큰 수를 계속 더하되 minNum번째 반복되면 그 다음으로 큰 수를 한번씩 더해준다.
-> 결국 가장 큰 수 가 더해지는 횟수는 maxNum을 minNum+1로 나눈 몫에 minNum을 곱한 값
    : 연속으로 같은 수가 minNum번 더해질 수 있는 횟수
   마지막에 minNum번까지는 못 더해지지만 그 보다 적게 더해질 수 있으므로 maxNum을 minNum+1로 나눈 나머지를 구해서 더하기

위 방법으로 구한 횟수만큼 가장 큰수를 곱해주고 남은 횟수는 그 다음으로 큰 수를 곱해주는 풀이
'''
count = int(maxNum/(minNum+1)) * minNum
count += maxNum % (minNum + 1)

result += count * firstNum
result += (maxNum - count) * secondNum

end_time = time.time()
print(result)
print(end_time - start_time)    # 9.059906005859375e-06
