from collections import deque
from itertools import combinations

N, M = map(int, input().split())
metrics = [list(map(int, input().split())) for _ in range(N)]

virus_arr = []
space_arr = []

# 바이러스와 공백 위치 저장
for i in range(N) :
    for j in range(M) :
        if metrics[i][j] == 2 :
            virus_arr.append((i, j))
        if metrics[i][j] == 0 :
            space_arr.append((i, j))


result = -1
for comb in combinations(space_arr, 3) :
    m = [[c for c in row] for row in metrics]
    q = deque()
    
    # 벽 설정
    for y, x in comb :
        m[y][x] = 1
    
    for y, x in virus_arr :
        q.append((y, x))

    while q :
        y, x = q.popleft()
        
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)] :
            nowy, nowx = y+dy, x+dx
            if 0 <= nowy < N and 0 <= nowx < M and m[nowy][nowx] == 0 :
                m[nowy][nowx] = 2
                q.append((nowy, nowx))
    
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if m[i][j] == 0 :
                cnt += 1
    result = max(result, cnt)

print(result)
    

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3
"""