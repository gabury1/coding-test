# [12100] 2048 Easy
# https://www.acmicpc.net/problem/12100
# 골드 2

import sys
from  collections import deque

input = sys.stdin.readline

# 슬라이드하는거, dir = U, D, L, R
def slide(dir) :

    global N, metrics
    result = 0
    if dir == 'U' :
        for x in range(N) :
            blocks = deque()
            for y in range(N) :
                if metrics[y][x] != 0 :
                    blocks.append(metrics[y][x])
                    metrics[y][x] = 0
            cnt = 0
            while blocks :
                first = blocks.popleft()
                metrics[cnt][x] = first
                if blocks :
                    second = blocks[0]
                    if second == first :
                        metrics[cnt][x] += second
                        blocks.popleft()
                result = max(result, metrics[cnt][x])
                cnt += 1
    if dir == 'D' :
        for x in range(N) :
            blocks = deque()
            for y in range(N-1, -1, -1) :
                if metrics[y][x] != 0 :
                    blocks.append(metrics[y][x])
                    metrics[y][x] = 0
            cnt = N-1
            while blocks :
                first = blocks.popleft()
                metrics[cnt][x] = first
                if blocks :
                    second = blocks[0]
                    if second == first :
                        metrics[cnt][x] += second
                        blocks.popleft()
                result = max(result, metrics[cnt][x])
                cnt -= 1
    
    if dir == 'L' :
        for y in range(N) :
            blocks = deque()
            for x in range(N) :
                if metrics[y][x] != 0 :
                    blocks.append(metrics[y][x])
                    metrics[y][x] = 0
            cnt = 0
            while blocks :
                first = blocks.popleft()
                metrics[y][cnt] = first
                if blocks :
                    second = blocks[0]
                    if second == first :
                        metrics[y][cnt] += second
                        blocks.popleft()
                result = max(result, metrics[y][cnt])
                cnt += 1

    if dir == 'R' :
        for y in range(N) :
            blocks = deque()
            for x in range(N-1, -1, -1) :
                if metrics[y][x] != 0 :
                    blocks.append(metrics[y][x])
                    metrics[y][x] = 0
            cnt = N-1
            while blocks :
                first = blocks.popleft()
                metrics[y][cnt] = first
                if blocks :
                    second = blocks[0]
                    if second == first :
                        metrics[y][cnt] += second
                        blocks.popleft()
                result = max(result, metrics[y][cnt])
                cnt -= 1
    

    return result

def dfs(index) :
    global N, metrics, result
    if index == 0 : 
        return
    
    origin = [[metrics[y][x] for x in range(N)] for y in range(N)]

    result = max(result, slide('U'))
    dfs(index-1)
    metrics = [[origin[y][x] for x in range(N)] for y in range(N)]

    result = max(result, slide('D'))
    dfs(index-1)
    metrics = [[origin[y][x] for x in range(N)] for y in range(N)]

    result = max(result, slide('L'))
    dfs(index-1)
    metrics = [[origin[y][x] for x in range(N)] for y in range(N)]

    result = max(result, slide('R'))
    dfs(index-1)
    metrics = [[origin[y][x] for x in range(N)] for y in range(N)]


N = int(input())
metrics = [list(map(int, input().split())) for _ in range(N)]
result = 0

dfs(5)
print(result)

"""
3
2 2 2
4 4 4
8 8 8

16

4
2 2 2 4
0 0 0 2
2 2 2 2
4 4 4 2

"""

"""
구현 겸 dfs 같은데

"""