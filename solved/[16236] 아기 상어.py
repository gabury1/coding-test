from collections import deque


def bfs(shark_y, shark_x, size) :
    global metric
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((shark_y, shark_x, 0))
    r_y, r_x = -1, -1
    r_dis = -1
    while q :
        y, x, dis = q.popleft()
        if 0 < metric[y][x] < size :
            if r_dis == -1 : 
                r_dis = dis
                r_y, r_x = y , x
            elif r_dis < dis : break
            elif r_dis == dis :
                if y < r_y :
                    r_y, r_x = y , x
                elif y == r_y :
                    if x < r_x :
                        r_x = x

                break
        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)] :
            now_y, now_x = y+dy, x+dx
            if 0 <= now_y < N and 0 <= now_x < N and not visited[now_y][now_x] :
                if metric[now_y][now_x] <= size :
                    visited[now_y][now_x] = True
                    q.append((now_y, now_x, dis+1))


    if r_dis != -1 : metric[r_y][r_x] = 0
    return r_y, r_x, r_dis
                         

N = int(input())
metric = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
eat_cnt = 0
size = 2
shark_y, shark_x = 0 , 0
for i in range(N) :
    for j in range(N) :
        if metric[i][j] == 9 :
            metric[i][j] = 0
            shark_y = i
            shark_x = j


while True :
    y, x, dis = bfs(shark_y, shark_x, size)

    if dis == -1 :
        break
    shark_y = y
    shark_x = x
    cnt += dis
    eat_cnt += 1
    if eat_cnt == size :
        eat_cnt = 0
        size += 1

print(cnt)

"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

14


6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

48

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

39

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

60
"""
