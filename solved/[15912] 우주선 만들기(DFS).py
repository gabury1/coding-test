
def dfs(left, right) :

    if dp[left][right] < float('inf') : 
        return dp[left][right]
    if left == right :
        dp[left][right] = w_arr[left] * e_arr[left]
        return dp[left][right]
    
    mw, me = m[left][right]
    cand = [mw*me]
    for i in range(left, right) :
        cand.append(dfs(left, i) + dfs(i+1, right))

    dp[left][right] = min(cand)
    return dp[left][right]
        



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


print(dfs(0, N-1))
print(*dp)


"""
5
1 2 3 4 5
3 2 8 9 4
45

5
10 9 1 7 6
4 2 99 4 3
167
"""