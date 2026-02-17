
def rotate(dir) :
    
    if dir == 0 : 
        return 3
    
    return dir - 1


N, M = map(int, input().split())
rn, rm, rdir = map(int, input().split())

# 0 : 빈 칸 1 : 벽 2 : 청소된 빈 칸 
metrics = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0

while(True) :

    # 현재 칸 청소
    if metrics[rn][rm] == 0 :
        metrics[rn][rm] = 2 # 청소된 빈 칸
        cnt += 1
    
    # 주변 4칸이 비었는지 확인
    empty_flag = True
    for dy, dx in dir :
        if metrics[rn + dy][rm + dx] == 0 :
            empty_flag = False
            break

    # 주변 네 칸이 비었다면?
    if empty_flag :
        dy, dx = dir[rdir]
        if metrics[rn - dy][rm - dx] != 1 :
            rn -= dy
            rm -= dx
            continue

        else  :
            break
    
    # 주변 네 칸이 청소 가능하면?
    elif not empty_flag : 

        rdir = rotate(rdir)
        while True :
            dy, dx = dir[rdir]
            if metrics[rn+dy][rm+dx] == 0 :
                break
            elif metrics[rn+dy][rm+dx] != 0 :
                rdir = rotate(rdir)

        dy, dx = dir[rdir]
        rn += dy
        rm += dx
        continue

print(cnt)





"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1

1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

57





5 5
2 1 1
1 1 1 1 1
1 0 0 0 1
1 0 1 1 1
1 0 0 0 1
1 1 1 1 1
"""