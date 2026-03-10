# [11967] 불켜기
# https://www.acmicpc.net/problem/11967
# 골드 2

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
switch = {}

for _ in range(M) :
    a,b,c,d = map(int, input().split())
    l = switch.get((a, b), [])
    l.append((c, d))
    switch[(a,b)] = l

# 0, 1 ,2 : 안가봄, 블락됨, 가봄
visited = [[0]*(N+1) for _ in range(N+1)]
lights = [[False]*(N+1) for _ in range(N+1)]
result = set()

q = deque()
q.append((1, 1))
lights[1][1] = True
result.add((1,1))


while q :
    y, x = q.popleft()

    s_list = switch.get((y, x), [])
    
    # 스위치를 켜주자
    for sy, sx in s_list :
        result.add((sy,sx))
        lights[sy][sx] = True
        # 블락 당한 이력이 있으면 큐에 넣어줌
        if visited[sy][sx] == 1 :
            visited[sy][sx] = 2
            q.append((sy, sx))
    
    # 상하좌우 이동
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
        ny, nx = y+dy, x+dx
        if 1 <= ny <= N and 1 <= nx <= N :
            if visited[ny][nx] : continue
            if lights[ny][nx] :
                visited[ny][nx] = 2
                q.append((ny, nx))
            else :
                # 블락됨으로 표시해둠
                visited[ny][nx] = 1

print(len(result))

"""
3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1

5
"""