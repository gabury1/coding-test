
def rotate(d) :
    global back
    if d == 1 :
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = back
        back = temp
    if d == 2 :
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = back
        back = temp
    if d == 3 :
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = back
        back = temp
    if d == 4 :
        temp = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = back
        back = temp

    return dice[1][1]



N, M, y, x, C = map(int, input().split())
metric = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
back = 0

for c in command :
    dy, dx = dir[c]
    if 0 <= y + dy < N and 0 <= x + dx < M :
        y += dy
        x += dx
        rotate(c)
        if metric[y][x] == 0 :
            metric[y][x] = back
        else :
            back = metric[y][x]
            metric[y][x] = 0
        print(dice[1][1])
        
        


"""
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

0
0
3
0
0
8
6
3

3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3

0
0
0
3
0
1
0
6
0

"""


