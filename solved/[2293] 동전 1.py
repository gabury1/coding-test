
N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

# DP 초기화
dp = [[0] * N for _ in range(K+1)]
for i in range(N) :
    dp[arr[i]][i] = 1

for i in range(1, K) :
    for j in range(N) :
        if i + arr[j] <= K :
            for k in range(j, N) :
                dp[i + arr[j]][j] += dp[i][k]

print(sum(dp[K]))

            


"""
3 10
1
2
5

10
"""