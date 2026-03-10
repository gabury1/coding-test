# [9328] 열쇠
# https://www.acmicpc.net/problem/9328
# 골드 1

import sys

input = sys.stdin.readline

T = int(input())
N, M = map(int, input().split())
visited = [[False]*M for _ in range(N)]



"""
진입점 별로, 몇개의 문서를 갖고 나올 수 있는지가 중요한거 같군.

3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony


3
1
0

"""