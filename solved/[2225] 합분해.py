# [2225] 합분해
# https://www.acmicpc.net/problem/2225
# 골드 5

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[1]*(N+1) for _ in range(K+1)]

for i in range(N+1) :
    dp[1][i] = 1

for i in range(2, K+1) :
    for j in range(1, N+1) :
        dp[i][j] = sum(dp[i-1][:j+1]) % 1000000000

print(dp[K][N])


"""
20 2
21

6 4
84

"""