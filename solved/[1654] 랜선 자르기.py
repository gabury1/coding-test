import sys
input = sys.stdin.readline

k, n = map(int, input().split(" "))
arr = [int(input()) for _ in range(k)]

left, right = 1, max(arr)

while left <= right :
    mid = (left + right) // 2
    lan_cnt = sum(lan//mid for lan in arr)

    if n <= lan_cnt :
        left = mid + 1
    else :
        right = mid - 1

print(right)

"""
4 11
802
743
457
539
"""