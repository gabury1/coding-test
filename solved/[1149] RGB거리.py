
N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*3 for _ in range(N)]
for i in range(3) :
    memo[0][i] = mtx[0][i]


for i in range(1, N) :
    
    for j in range(3) :
        cand = []
        for prev_j in range(3) :
            if prev_j != j :
                cand.append(memo[i-1][prev_j])
        
        memo[i][j] = min(cand) + mtx[i][j]


print(min(memo[N-1]))

"""
3
26 40 83
49 60 57
13 89 99

96
"""
