# [2293] 동전 1
# https://www.acmicpc.net/problem/2293
# 골드 5

import sys

input = sys.stdin.readline


N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

dp = [1] + [0] * K


for coin in arr :
    for i in range(coin, K+1) :
        dp[i] += dp[i-coin] 

print(dp[K])



"""
3 10
1
2
5

10
"""