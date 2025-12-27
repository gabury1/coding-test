from collections import deque

n, m = map(int, input().split(" ")) # n : 세로, m : 가로
mtx = [list(map(int, input().split())) for _ in range(n)]
result_mtx = [[-1]*m for _ in range(n)]
chk_mtx = [[False]*m for _ in range(n)]

q = deque()
for i in range(n) :
    for j in range(m) :
        if mtx[i][j] == 2 :
           q.append((i, j, 0))
           chk_mtx[i][j] = True

while q :
    y, x, lev = q.popleft()

    if mtx[y][x] == 0 :
        result_mtx[y][x] = 0
        continue

    result_mtx[y][x] = lev
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)] :

        if not (0<=x+dx<m and 0<=y+dy<n) or chk_mtx[y+dy][x+dx] :
            continue

        chk_mtx[y+dy][x+dx] = True
        q.append((y+dy, x+dx, lev+1))




for i in range(n) :
    for j in range(m) :
        print(result_mtx[i][j] if mtx[i][j] != 0 else 0, end=" ")
    print("\n", end="")

"""
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 0 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
"""