
T = int(input()) # 테스트 케이스 수

for _ in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    # (여기까지 오기까지 최소의 합, 비용)
    dp = [[0] * N for _ in range(N)]

    for offset in range(2, N+1) :
        for i in range(N-offset+1) :
            mini = float("inf")
            val = sum(arr[i : i+offset])
            for j in range(i, i+offset-1) : # i ~ i + offset-1\
                #print(f"{i} {j} , {j+1} {i+offset-1}")
                mini = min(mini, dp[i][j] + dp[j+1][i+offset-1] + val)

            dp[i][i+offset-1] = mini
    
    print(dp[0][N-1])

"""
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

"""