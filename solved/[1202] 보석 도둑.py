# [1202] 보석 도둑
# https://www.acmicpc.net/problem/1202

import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jems = [tuple(map(int, input().split())) for _ in range(N)] # 무게 , 가치
jems.sort(key=lambda x : x[0])
bags = [int(input()) for _ in range(K)]
bags.sort()


q = []
j_idx = 0
sum = 0
for b in bags :
    while j_idx < N and jems[j_idx][0] <= b :
        w, v = jems[j_idx]
        j_idx += 1
        heapq.heappush(q, -v)

    if q : v = -heapq.heappop(q)
    else : continue
    sum += v

print(sum)


"""
3 2
1 65
5 23
2 99
10
2

164


2 1
5 10
100 100
11

10

1 1
2 1
1

"""

"""

가방 하나가 가장 가치 있어지는 경우
개비싼 보석을 딱 맞게 넣었을 경우!

보석은 가치를 기준으로 내림차순,
가방은 무게 기준 오름차순으로 정렬.



"""