'''
p.113 시각
00시 00분 00초 ~ N시 59분 59초 사이에 3이 한번이라도 나오는 경우의 수 구하기
하루는 86400초이므로 경우의 수가 10만개를 넘지 않는다. 즉, 3중 반복문 사용 가능 -> 완전 탐색
** 완전 탐색 : 비효율적인 시간 복잡도를 가짐, 데이터 개수가 적을 때만 사용가능
'''
N = int(input())

cnt = 0

for hour in range(N+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour)+str(min)+str(sec):
                cnt += 1

print(cnt)