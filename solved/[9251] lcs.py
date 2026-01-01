str1 = input()
str2 = input()

# 2차원 DP 테이블
dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

# 테이블 채우기
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            # 같으면: 둘 다 전진 +1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 다르면: 둘 중 하나만 전진, 최대값
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])



print(dp[len(str1)][len(str2)])


"""
ACAYKP
CAPCAK

4
"""
