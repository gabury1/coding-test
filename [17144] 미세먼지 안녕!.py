from math import floor

def blow_top() :
    global top, metric
    # 좌측
    for i in range(top-1, -1, -1) : 
        metric[i][0] = metric[i-1][0]

    # 상단
    for i in range(C-1) :
        metric[0][i] = metric[0][i+1]

    # 우측
    for i in range(top) :
        metric[i][C-1] = metric[i+1][C-1]

    # 하단
    for i in range(C-1, 0, -1) :
        metric[top][i] = metric[top][i-1]

    metric[top][1] = 0

def blow_bottom() :
    global bottom, metric
    # 좌측
    for i in range(bottom+1, R-1) :
        metric[i][0] = metric[i+1][0]

    # 하단
    for i in range(C-1) :
        metric[R-1][i] = metric[R-1][i+1]

    # 우측
    for i in range(R-1, bottom-1, -1) :
        metric[i][C-1] = metric[i-1][C-1]

    # 상단
    for i in range(C-1, 0, -1) :
        metric[bottom][i] = metric[bottom][i-1]


    metric[bottom][1] = 0

def bourne() :

    global metric
    plus_metric = [[0]*C for _ in range(R)]

    for i in range(R) :
        for j in range(C) :
            amount = floor( metric[i][j] / 5)
            if 0 < metric[i][j]:
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
                    if 0 <= i + dy < R and 0 <= j + dx < C and metric[i+dy][j+dx] != -1 :
                        plus_metric[i+dy][j+dx] += amount
                        plus_metric[i][j] -= amount
    
    for i in range(R) :
        for j in range(C) :
            metric[i][j] += plus_metric[i][j]


R, C, T = map(int, input().split()) # R : 행 C : 열

metric = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 초기화
top, bottom = 0, 0
for i in range(R) :
    if metric[i][0] == -1 :
        top = i
        bottom = i+1
        break 

for _ in range(T) :
    bourne()
    blow_top()
    blow_bottom()

sum = 0

#print()
for i in range(R) :
    for j in range(C) :
        #print(metric[i][j], end=" ")
        if 0 < metric[i][j] :
            sum += metric[i][j]
    #print()
    

print(sum)




"""
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

188
"""