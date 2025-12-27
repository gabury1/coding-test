import sys
sys.setrecursionlimit(6**10)

def dfs(color, y, x) :
    if not (0 <= y < N and 0 <= x < N) or mtx[y][x] != color or normal_chk_mtx[y][x] == True:
        return

    normal_chk_mtx[y][x] = True
    if color == "B" : special_chk_mtx[y][x] = True
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
        dfs(color, y + dy , x + dx)


def special_dfs(y, x) :
    if not (0 <= y < N and 0 <= x < N) or mtx[y][x] == 'B' or special_chk_mtx[y][x] == True:
        return

    special_chk_mtx[y][x] = True
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
        special_dfs(y + dy , x + dx)


N = int(input())
mtx = [input() for _ in range(N)]
normal_chk_mtx = [[False]*N for _ in range(N)]
special_chk_mtx = [[False]*N for _ in range(N)]

normal_cnt = 0
special_cnt = 0
for i in range(N) :
    for j in range(N) :
        if mtx[i][j] == 'B' :
            if not normal_chk_mtx[i][j] :
                dfs(mtx[i][j], i, j)
                normal_cnt += 1
                special_cnt += 1
        else :
            if not normal_chk_mtx[i][j] :
                dfs(mtx[i][j], i, j)
                normal_cnt += 1
            if not special_chk_mtx[i][j] :
                special_dfs(i, j)
                special_cnt += 1

print(f"{normal_cnt} {special_cnt}")

"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

4 3
"""