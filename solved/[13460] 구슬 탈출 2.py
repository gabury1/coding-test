# [13460] 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
# 골드 1

import sys
from collections import deque
def slide(dir, red, blue) :
    dy, dx = 0, 0
    ry, rx = red
    by, bx = blue
    match dir :
        case 'U' : dy = -1
        case 'D' : dy = 1
        case 'L' : dx = -1
        case 'R' : dx = 1

    metrics[ry][rx] = 'R'
    metrics[by][bx] = 'B'

    while metrics[ry+dy][rx+dx] == '.' or metrics[ry+dy][rx+dx] == 'O' \
        or metrics[by+dy][bx+dx] == '.' or metrics[by+dy][bx+dx] == 'O' :

        if not ry == rx == -1:
            if metrics[ry+dy][rx+dx] == '.' :
                metrics[ry][rx] = '.'
                metrics[ry+dy][rx+dx] = 'R'
                ry += dy
                rx += dx
            elif metrics[ry+dy][rx+dx] == 'O' :
                metrics[ry][rx] = '.'
                ry = rx = -1
        if not by == bx == -1 :
            if metrics[by+dy][bx+dx] == '.' :
                metrics[by][bx] = '.'
                metrics[by+dy][bx+dx] = 'B'
                by += dy
                bx += dx
            elif metrics[by+dy][bx+dx] == 'O' :
                metrics[by][bx] = '.'
                by = bx = -1
    if ry != -1 :
        metrics[ry][rx] = '.'
    if by != -1 :
        metrics[by][bx] = '.'

    return (ry, rx, by, bx)


input = sys.stdin.readline
N, M = map(int, input().split())
metrics = [list(input()[:-1]) for _ in range(N)]
red_origin = (0, 0)
blue_origin = (0, 0)
for i in range(N) :
    for j in range(M) :
        if metrics[i][j] == 'R' :
            red_origin = (i, j)
            metrics[i][j] = '.'
        elif metrics[i][j] == 'B' :
            blue_origin = (i, j)
            metrics[i][j] = '.'

q = deque()
# 이전 메소드, cnt, ry, rx, by, bx
q.append(('pre', 0, red_origin[0], red_origin[1], blue_origin[0], blue_origin[1]))

result = -1
while q :
    pre, cnt, ry, rx, by, bx = q.popleft()
    if cnt == 10 : break

    for method in ['U', 'D', 'L', 'R'] :
        if pre == method :
            continue
        if method == 'U' and pre == 'D' :
            continue
        if method == 'D' and pre == 'U' :
            continue
        if method == 'L' and pre == 'R' :
            continue
        if method == 'R' and pre == 'L' :
            continue

        nry, nrx, nby, nbx = slide(method, (ry, rx), (by, bx))
        if nby == -1 :
            continue
        if nry == -1 :
            result = cnt+1
            break
        q.append((method, cnt+1, nry, nrx, nby, nbx))

    if result != -1 :
        break

print(result)



"""
BFS 구현 계획
1. slide() 구현
2. BFS 구현



5 5
#####
#..B#
#.#.#
#RO.#
#####

1

7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

5


5 5
#####
#...#
#.#B#
#.OR#
#####

"""