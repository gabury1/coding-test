
N = int(input())
arr = [int(input()) for _ in range(N)]

# dp[i][0] = 한칸 뛰기 dp[i][1] = 두칸 뛰기
dp = [[0] * 2 for _ in range(N)]

dp[0][0] = arr[0]
dp[0][1] = -1
if 1 < N :
    dp[1][0] = dp[0][0] + arr[1]
    dp[1][1] = arr[1]
    
for i in range(2, N) :
    now = arr[i]
    # 한 칸 뛰기 (이전에 두 칸 뛰기를 했어야 함.)
    dp[i][0] = dp[i-1][1] + now
    # 두 칸 뛰기
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + now

print(max(dp[N-1]))

"""
6
10
20
15
25
10
20

75
"""