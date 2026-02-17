# [9663] N-Queen
# https://www.acmicpc.net/problem/9663
# Gold 4

import sys
sys.setrecursionlimit(6**10)

N = int(input())
middle = N - 1

rows = [False] * N
columns = [False] * N
cross_left = [False] * (N*2 - 1)
cross_right = [False] * (N*2 - 1)

def dfs(y):
    if y == N:
        return 1

    result = 0
    for x in range(N):
        # check - 이미 공격받는 위치면 skip
        if rows[y] or columns[x] or cross_left[y+x] or cross_right[middle-y+x]:
            continue

        # marking
        rows[y] = columns[x] = cross_left[y+x] = cross_right[middle-y+x] = True
        result += dfs(y+1)
        # backtrack
        rows[y] = columns[x] = cross_left[y+x] = cross_right[middle-y+x] = False

    return result

print(dfs(0))