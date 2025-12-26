import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split(" ")) # x y z = n m h

# 입력부
metric = [[list(map(int, input().split(" "))) for _ in range(m)] for _ in range(h)]


q = deque()
tomato_cnt = 0 # 익어야할 토마토 개수
for k in range(h) :
    for i in range(m) :
        for j in range(n) :
            if metric[k][i][j] == 1 :
                q.append((k, i, j, 0)) # z, y, x, days

            elif metric[k][i][j] == 0 :
                tomato_cnt += 1

last_days = 0 # 마지막으로 익은 토마토의 날짜 수
while q :
    z, y, x, days = q.popleft()
    last_days = days
    for dz, dy, dx in [(1, 0 , 0) , (0, 1, 0), (0, 0, 1), (-1, 0 , 0), (0, -1, 0), (0, 0 ,-1)] :
        nz, ny, nx = z+dz, y+dy, x+dx
        if (0 <= nz < h and 0 <= ny < m and 0 <= nx < n) and metric[nz][ny][nx] == 0 : 
            metric[nz][ny][nx] = 1
            tomato_cnt -= 1
            q.append((nz, ny, nx, days+1))

if tomato_cnt == 0 :
    print(last_days)
else : print(-1)
