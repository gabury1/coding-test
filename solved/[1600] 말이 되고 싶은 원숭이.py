from collections import deque

K = int(input())
W, H = map(int, input().split())
metrics = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False]*(K+1) for _ in range(W)] for _ in range(H)] #[H][W][사용한 말행동개수]

q = deque()
q.append((0,0,K, 0))
visited[0][0][K] = True

result = -1
while q :
    y, x, jumps, cnt = q.popleft()
    if y == H-1 and x == W-1 :
        result = cnt
        break

    if 0 < jumps :
        for dy, dx in [(-2, -1), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2), (2, 1), (1, 2)] :
            nowy, nowx = y+dy, x+dx
            if 0 <= nowy < H and 0 <= nowx < W and metrics[nowy][nowx] != 1 and not visited[nowy][nowx][jumps-1] :
                visited[nowy][nowx][jumps-1] = True
                q.append((nowy, nowx, jumps-1, cnt+1))
    
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
        nowy, nowx = y+dy, x+dx
        if 0 <= nowy < H and 0 <= nowx < W and metrics[nowy][nowx] != 1 and not visited[nowy][nowx][jumps] :
            visited[nowy][nowx][jumps] = True
            q.append((nowy, nowx, jumps, cnt+1))
    
print(result)








"""
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

4

"""