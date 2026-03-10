# [1541] 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 실버 2

import sys

input = sys.stdin.readline

m = input().split('-')
num = []
for p in m :
    n = sum(list(map(int, p.split('+'))))
    num.append(n)

if len(num) == 1 :
    print(num[0])
else :
    print(num[0] - sum(num[1:]))





"""
55-50+40

-35

00009-00009
0
"""
