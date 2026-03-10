# [16946] 벽 부수고 이동하기 4
# https://www.acmicpc.net/problem/16946
# 골드 2

import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x, id) :
    global N, M, union, dir, metrics
    q = deque()
    q.append((y, x))

    cnt = 0
    while q :
        r, c = q.popleft()
        if union[r][c] != -1 :
            continue
        cnt+=1
        union[r][c] = id
        
        for dy, dx in dir :
            ny, nx = r+dy, c+dx
            if 0<=ny<N and 0<=nx<M and metrics[ny][nx] == 0 and union[ny][nx] == -1 :
                q.append((ny, nx))
    
    return cnt


N, M = map(int, input().split())
metrics = [list(map(int, input()[:-1])) for _ in range(N)]
union = [[-1 for x in range(M)] for y in range(N)]
near_dict = {}
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


                

# 먼저 유니온 파인드로 영역 정의 , 각 영역이 몇개의 인접요소들을 가진지 dict로 표현
id = 0
for y in range(N) :
    for x in range(M) :

        # 연결된 노드가 없을때(완전히 새로운 영역)
        if metrics[y][x] == 0 and union[y][x] == -1 :
            cnt = bfs(y, x, id)
            near_dict[id] = cnt
            id+=1


result = [[0]*M for _ in range(N)]
for y in range(N) :
    for x in range(M) :
        ids = set()
        if metrics[y][x] == 1 :
            for dy, dx in dir :
                ny, nx = y+dy, x+dx
                if 0<=ny<N and 0<=nx<M and union[ny][nx] != -1 :
                    ids.add(union[ny][nx])
            result[y][x] = (sum([near_dict[id] for id in ids])+1) % 10

for y in range(N) :
    for x in range(M) :
        print(result[y][x], end="")
    print()




"""
3 3
101
010
101

303
050
303

4 5
11001
00111
01010
10101

46003
00732
06040
50403

1 1
1

"""