
N = int(input())
w_arr = list(map(int, input().split()))
e_arr = list(map(int, input().split()))

# 구간 별 w,e의 최대값들이 들어갈 배열
m = [[(0,0)]*N for _ in range(N) ] # (w, e)
# dp (구간 별 가격 최대값들이 들어감)
dp = [[float('inf')]*N for _ in range(N)]

# 구간별 최대값 초기화
for i in range(N) :
    for j in range(i, N) :
        if i==j :
            m[i][j] = (w_arr[i], e_arr[i])
        else :
            w, e = m[i][j-1]
            m[i][j] = (max(w_arr[j], w), max(e_arr[j], e))

for idx, (w, e) in enumerate(zip(w_arr, e_arr)) :
    dp[idx][idx] = w*e

for limit in range(N) :
    for left in range(N - limit) :
        right = left + limit
        mw, me = m[left][right]
        cand = [mw*me]
        for mid in range(left, right) :
            cand.append( dp[left][mid] + dp[mid+1][right])
        dp[left][right] = min(cand)
        
print(dp[0][N-1])


"""
5
1 2 3 4 5
3 2 8 9 4
45

5
10 9 1 7 6
4 2 99 4 3
167

5
0 9 1 7 6
4 2 99 4 3
167
"""