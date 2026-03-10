# [2294] 동전 2
# https://www.acmicpc.net/problem/2294
# 골드 5

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [0] + [float('inf')] * (K)

for coin in arr :
    if K < coin : continue
    for i in range(coin, K+1) :
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[K] if dp[K]!=float('inf') else -1)




"""
3 15
1
5
12

3

3 15
11
22
32


"""
