# [1699] 제곱수의 합
# https://www.acmicpc.net/problem/1699
# 실버 2

import sys

input = sys.stdin.readline
N = int(input())
dp = [0] + [0] * N


for i in range(1, N+1) :
    
    result = float('inf')
    square = 1
    while square**2 <= i :
        result = min(result, dp[i - square**2] + 1)
        square = (square+1)

    dp[i] = result


print(dp[N])
"""
7

4
"""
