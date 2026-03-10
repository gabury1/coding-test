# [1806] 부분합
# https://www.acmicpc.net/problem/1806
# 골드 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
now = arr[0]
result = float('inf')
while left < N and right < N : 
    
    if M <= now :  
        result = min(result, abs(left-right)+1)
        if left == right :
            left += 1
            right += 1
            if left < N :now = arr[left]
        else :
            now -= arr[left]
            left += 1
    else :
        right += 1
        if right < N : now += arr[right]
        
print(result if result != float('inf') else 0)

"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

그냥... 구간 DP

10 15
5 1 3 5 10 7 4 9 2 8

2


"""