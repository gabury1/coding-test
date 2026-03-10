# [2342] Dance Dance Revolution
# https://www.acmicpc.net/problem/2342
# 골드 3

import sys
from collections import deque

input = sys.stdin.readline
arr = list(map(int, input().split()[:-1]))

def get_energy(start, end) :
    if start == 0 :
        return 2
    if start == end : return 1

    if abs(start-end) == 2 :
        return 4
    else : 
        return 3
    
dp = [[[float('inf')]*5 for _ in range(5)] for  _ in range(len(arr))]
dp[0][arr[0]][0] = dp[0][0][arr[0]] = 2


for i in range(1, len(arr)) :
    now = arr[i]
    for left in range(5) :
        for right in range(5) :
            if dp[i-1][left][right] != float('inf') :
                dp[i][left][now] = min(dp[i][left][now], dp[i-1][left][right]+get_energy(right, now))
                dp[i][now][right] = min(dp[i][now][right], dp[i-1][left][right]+get_energy(left, now))

result = float('inf')
for l in dp[len(arr)-1] :
    for c in l :
        result = min(result, c)

print(result)
"""
1 2 2 4 0
8
"""