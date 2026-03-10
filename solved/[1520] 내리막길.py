# [1520] 내리막길
# https://www.acmicpc.net/problem/1520
# 골드 3

import sys
from collections import deque


sys.setrecursionlimit(6**10)
def dfs(y, x) :
    if y==M-1 and x==N-1 : return 1
    if dp[y][x] != -1 : return dp[y][x]

    cnt = 0
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        ny, nx = dy+y, dx+x
        if 0<=ny<M and 0<=nx<N and metrics[ny][nx] < metrics[y][x] :
            if dp[ny][nx] != -1 :
                cnt += dp[ny][nx]
            else :
                cnt += dfs(ny, nx)
    dp[y][x] = cnt
    return dp[y][x]


input = sys.stdin.readline
# 세로 가로
M, N = map(int , input().split())
metrics = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]

print(dfs(0, 0))




"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

3
"""
