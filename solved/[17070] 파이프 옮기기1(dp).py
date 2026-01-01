
def pipe_check(type, r, c) :
    match type :
        case 0 :
            for i in range(2) :
                if not 0<=c+i<N or mtx[r][c+i] == 1 : 
                    return True
        case 1 :
            for i in range(2) :
                for j in range(2) :
                    if not (0<=c+j<N and 0<=r+i<N) or mtx[r+i][c+j] == 1 : 
                        return True
        case 2 : 
            for i in range(2) :
                if not 0<=r+i<N or mtx[r+i][c] == 1 : 
                    return True
    return False
                            


N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]
memo = [[[0] * N for _ in range(N)] for _ in range(3)]

# 베이스 케이스: 목표 지점 도달
# 대각선: 4칸 모두 0이어야 함
if mtx[N-2][N-2] == 0 and mtx[N-2][N-1] == 0 and mtx[N-1][N-2] == 0 and mtx[N-1][N-1] == 0:
    memo[1][N-2][N-2] = 1

# 가로: 2칸 모두 0이어야 함
if mtx[N-1][N-2] == 0 and mtx[N-1][N-1] == 0:
    memo[0][N-1][N-2] = 1

# 세로: 2칸 모두 0이어야 함
if mtx[N-2][N-1] == 0 and mtx[N-1][N-1] == 0:
    memo[2][N-2][N-1] = 1

for i in range(N-1, -1, -1) :
    for j in range(N-1, -1, -1) :
        if N-2<=i<N and N-2<=j<N : continue

        for type in range(3) :
            if pipe_check(type, i, j) : continue
            match type :
                case 0 :
                    memo[0][i][j] = memo[0][i][j+1] + memo[1][i][j+1]
                case 1 :
                    memo[1][i][j] = memo[0][i+1][j+1] + memo[1][i+1][j+1] + memo[2][i+1][j+1]
                case 2 : 
                    memo[2][i][j] = memo[1][i+1][j] + memo[2][i+1][j]

print(memo[0][0][0])


"""
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

3
0 0 0
0 0 0
0 0 0

16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
"""

"""
최초 시도, 구현 + DP로 풀 생각.
1. memo[r,c,t] ((r,c)의 위치에서 t 형태일때) 답으로 가는 가짓 수는 정해져있다고 가정.

생각한게 맞았다! 하지만 문제를 제대로 이해하지 못해 애먹었다...
바텀업도 해봐야지 !
"""