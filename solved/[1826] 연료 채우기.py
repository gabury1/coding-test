# [1826] 연료 채우기
# https://www.acmicpc.net/problem/1826
# 골드 3

import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input()) # 주유소 개수
# 주유소 정보
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()
arr = deque(arr)

# 마을 거리, 기본 연료
L, P = map(int, input().split())
# 지금 연료로 갈 수 있는 주유소들을 q에 넣어줌
q = []

while arr and arr[0][0] <= P :
    d, f = arr.popleft()
    heapq.heappush(q, -f)


dis, cnt = P, 0
while q :

    # 잔존 연료로 마을까지 갈 수 있으면 종료
    if L <= dis : break 

    cnt += 1
    refuel = -heapq.heappop(q)
    dis += refuel

    while arr and arr[0][0] <= dis :
        d, f = arr.popleft()
        heapq.heappush(q, -f)

print(cnt if L <= dis else -1)


"""
4
4 4
5 2
11 5
15 10
25 10

3

1
1 1
100 1

1
1 1
24 25




"""
