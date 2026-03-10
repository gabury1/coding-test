# [2457] 공주님의 정원
# https://www.acmicpc.net/problem/2457
# 골드 3

import sys
from datetime import date
import heapq
from collections import deque
input = sys.stdin.readline

months = {1 : 31, 2 : 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr = [(date(2026, sm, sd), (date(2026, 3, 1) - date(2026, em, ed))) for sm, sd, em, ed in arr if 3 <= em]
arr.sort()
arr = deque(arr)

q = []
now = date(2026, 3, 1)
cnt = 0

while arr and arr[0][0] <= now :
    start_date, duration_days = arr.popleft()
    heapq.heappush(q, duration_days)

while q and now <= date(2026, 11, 30):
    # 만일 꽃의 시작날짜가 지금 날짜보다 같거나 작으면 심을 수 있음.
    while q :
        end_date = date(2026,3,1) - heapq.heappop(q)
        if now < end_date :
            now = end_date
            cnt+=1

    # 꽃 중 가장 오래 피되, 지금 꽃보다 멀리 피는거 선택. 그게 아니면 다 버림.
    while arr and arr[0][0] <= now :
        start_date, duration_days = arr.popleft()
        heapq.heappush(q, duration_days)

# 2026-12-01 에 꽃이 져야함. 혹은 그 뒤
print(cnt if date(2026, 12, 1) <= now else 0 )




"""
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10

2


"""
