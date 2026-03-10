# [2805] 나무 자르기
# https://www.acmicpc.net/problem/2805
# 실버 2

import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

left, right = 1, max(arr)

while left <= right :
    mid = (left + right) // 2
    total = sum(map(lambda x : x - mid if x > mid else 0, arr))

    if M <= total :
        left = mid + 1
    else :
        right = mid -1
    
print(right)

#while left <= right :
#    mid = (left + right) // 2
#
#    total_tree = sum(map(lambda tree : (tree-mid) if mid < tree else 0, arr))
#
#    if M <= total_tree :
#        left = mid + 1
#    else :
#        right = mid - 1
#
#print(right)
