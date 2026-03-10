# [7579] 앱
# https://www.acmicpc.net/problem/7579
# 골드 3

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [(c, m) for m, c in zip(map(int, input().split()), map(int, input().split()))] # 최대 100

dp = {0 : 0}

for c, m in arr :
    items = [(k, v) for k, v in dp.items()]
    for kCost, vMem in items :
        if kCost+c in dp :
            if vMem + m > dp[kCost+c] :
                dp[kCost+c] = vMem + m
        else :
            dp[kCost+c] = vMem + m

result = min(k for k, v in dp.items() if v >= M)
print(result)


"""
5 60
30 10 20 35 40
3 0 3 5 4

6
"""
