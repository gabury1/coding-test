# [11049] 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049
# 골드 3

import sys

input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf'), 0, 0] for _ in range(N)] for _ in range(N)] # (total, left, right)

for i in range(N) :
    dp[i][i] = (0, arr[i][0], arr[i][1])

for limit in range(1, N) :
    for i in range(0, N-limit) :
        mini = (float('inf'), 0 , 0)
        for mid_idx in range(i, i+limit) :
            total_left, left, mid = dp[i][mid_idx]
            total_right, mid, right = dp[mid_idx+1][i+limit]
            total = (total_left+total_right+left*mid*right, left, right)
            mini = min(mini, total)
        dp[i][i+limit] = mini

print(dp[0][N-1][0])

            

        



"""
3
5 3
3 2
2 6

90
"""
