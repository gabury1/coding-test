# [20040] 사이클 게임
# https://www.acmicpc.net/problem/20040
# 골드 4

import sys

sys.setrecursionlimit(6**10)
input = sys.stdin.readline

def find(node) :
    global parents
    if parents[node] == node :
        return node
    else :
        parents[node] = find(parents[node])
        return parents[node]

N, M = map(int, input().split())
parents = [i for i in range(N)]

for i in range(M) :

    a, b = map(int, input().split())
    if find(a) == find(b) :
        print(i+1)
        sys.exit()
    parents[find(b)] = find(a)

print(0)

"""
6 5
0 1
1 2
1 3
0 3
4 5

4

6 5
0 1
1 2
2 3
5 4
0 4

0


4 3
0 1
2 3
1 3

3
"""