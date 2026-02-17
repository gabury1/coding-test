
N = int(input())
metric = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

# 초깃값 세팅
for i in range(3) :
    dp[0][i] = metric[0][i]

for i in range(1, N) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + metric[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + metric[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + metric[i][2]

print(min(dp[N-1]))



"""
3
26 40 83
49 60 57
13 89 99

96
"""