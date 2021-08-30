'''
p.99 1이 될 때까지
k : 나눠줄 수 있는 숫자
n에 주어진 숫자를 1이 될때까지 (1씩 빼주기, k로 나눠주기) 둘 중 하나를 진행
k로 나눠주는 것은 나머지없이 딱 떨어질 때만 이용 가능
'''


import time

n, k = map(int, input().split())
cnt = 0

start_time = time.time()

'''
>> 내 풀이 <<
while True:
    if n == 1:
        break

    if n % k == 0:
        n //= k
    else:
        n -= 1

    cnt += 1

print(cnt)
end_time = time.time()
print(end_time - start_time)    # 4.291534423828125e-05
'''

'''
1. 책의 첫번째 풀이 : 단순풀이
while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

while n > 1:
    n -= 1
    cnt += 1

print(cnt)
end_time = time.time()
print(end_time - start_time)    # 2.8133392333984375e-05
'''

# 2. 책의 두번째 풀이 : 효율 고려
# n이 k의 배수가 되도록 만들어준 후 나누기 실행
while True:
    target = (n//k) * k
    cnt += n-target
    n = target

    if n < k:
        break
    cnt += 1
    n //= k

cnt += (n-1)
print(cnt)
end_time = time.time()
print(end_time - start_time)