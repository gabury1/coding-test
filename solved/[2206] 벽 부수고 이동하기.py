import sys
from collections import deque
sys.setrecursionlimit(6**10)


N, M = map(int, input().split())
metric = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] =  1
q = deque()
# y, x, cnt, 벽부수기 가능 여부
q.append((0, 0, 1, 1))

result = -1
while q :
    y, x, cnt, drill = q.popleft()
    if y == N-1 and x == M-1 :
        result = cnt
        break
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)] :
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M :
            if metric[ny][nx] == 1 :
                if visited[ny][nx][0] == 0  and drill==1 :
                    visited[ny][nx][0] = 1
                    q.append((ny, nx, cnt+1, 0))
            else :
                if visited[ny][nx][drill] == 0 :
                    visited[ny][nx][drill] = 1
                    q.append((ny, nx, cnt+1, drill))


print(result)


"""
6 4
0100
1110
1000
0000
0111
0000

15 

4 4
0111
1111
1111
1110
-1
"""