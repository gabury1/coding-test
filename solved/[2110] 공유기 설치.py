# [2110] 공유기 설치
# https://www.acmicpc.net/problem/2110
# 골드 4

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

lo, hi = 1, houses[-1] - houses[0]
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2

    # mid 간격 이상으로 C개 설치 가능한지 검증
    count = 1
    last = houses[0]
    for i in range(1, N):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    if count >= C:
        ans = mid
        lo = mid + 1  # 간격 더 넓혀보기
    else:
        hi = mid - 1  # 간격 줄이기

print(ans)


"""
5 3
1
2
8
4
9

3
"""
