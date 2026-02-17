from collections import deque
from itertools import combinations

N, M = map(int, input().split())
metric = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empty = 0

for i in range(N):
    for j in range(N):
        if metric[i][j] == 0:
            empty += 1
        elif metric[i][j] == 2:
            viruses.append((i, j))

result = float('inf')

for comb in combinations(viruses, M):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    
    for vy, vx in comb:
        q.append((vy, vx, 0))
        visited[vy][vx] = True
    
    max_time = 0
    infected = 0
    
    while q:
        y, x, time = q.popleft()
        
        for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
            ny, nx = y+dy, x+dx
            
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if metric[ny][nx] != 1:  # 벽 아니면
                    visited[ny][nx] = True
                    q.append((ny, nx, time+1))
                    
                    if metric[ny][nx] == 0:  # 빈 칸만 카운트
                        infected += 1
                        max_time = time + 1
    
    if infected == empty:
        result = min(result, max_time)

print(-1 if result == float('inf') else result)