
N = int(input())
arr = list(map(int, input().split()))
# 0 : 증가 중인 부분 수열 1 : 감소 중인 부분 수열
dp = [[0]*2 for _ in range(N)]

dp[0][0] = 1
dp[0][1] = 1

for i in range(1, N) :
    
    for j in range(i) :
        # 증가 중 일때
        if arr[j] < arr[i] :
            dp[i][0] = max(dp[j][0], dp[i][0])

        if arr[i] < arr[j] :
            dp[i][1] = max(dp[j][1], dp[j][0], dp[i][1])
    dp[i][0] += 1
    dp[i][1] += 1


result = 0
for i in range(N) :
    result = max(max(dp[i]), result)

print(result)
            

"""
10
1 5 2 1 4 3 4 5 2 1

7
"""