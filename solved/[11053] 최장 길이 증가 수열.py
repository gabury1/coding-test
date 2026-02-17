
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N) :
    dp[i] = 1
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

"""
6
10 20 10 30 20 50

4
"""