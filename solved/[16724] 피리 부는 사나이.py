# [16724] 피리 부는 사나이
# https://www.acmicpc.net/problem/16724
# 골드 3

import sys

input = sys.stdin.readline

# r, c
N, M = map(int, input().split())
metrics = [input() for _ in range(N)]
union = [[-1 for x in range(M)] for y in range(N)]


# DFS 진행하며 유니온 파인드 군집을 찾음.
def dfs(y, x, id) :

    if not (0 <= y < N and 0 <= x < M):
        return id

    if union[y][x] != -1 :
        return union[y][x]

    union[y][x] = id
    match metrics[y][x] :
        case 'U' : 
            next = dfs(y-1, x, id)
        case 'D' :
            next = dfs(y+1, x, id)
        case 'L' :
            next = dfs(y, x-1, id)
        case 'R' :
            next = dfs(y, x+1, id)
    
    union[y][x] = next
    return next


result = set()
cnt_id = 0
for r in range(N) :
    for c in range(M) :
        if union[r][c] == -1 :
            cnt_id += 1
            root = dfs(r, c, cnt_id)
            result.add(root)
            
print(len(result))




"""
유니온 파인드? 유니온 파인드 맞는거 같은데..
뭉치들의 개수가 곧 셸터의 개수니까.

3 4
DLLL
DRLU
RRRU

2


"""