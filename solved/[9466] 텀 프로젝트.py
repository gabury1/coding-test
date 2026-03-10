# [9466] 텀 프로젝트
# https://www.acmicpc.net/problem/9466
# 골드 3

import sys
input = sys.stdin.readline
sys.setrecursionlimit(6**10)


def dfs(node) :

    if visited[node] :
        return (node, True, 0)
    
    visited[node] = True
    last_node, cycle, cnt = dfs(out_arr[node])
    if cycle : cnt += 1
    return (last_node, cycle if node != last_node else not cycle, cnt)


T = int(input())
for _ in range(T) :
    N = int(input())
    # 지명한 대상이 누구인지
    out_arr = [-1] + list(map(int, input().split()))
    # 탐색 했었나?
    visited = [True] + [False] * (N)

    sum = 0
    for i, n in enumerate(out_arr) :

        if not visited[i] :
            last_node, cycle, cnt = dfs(i)
            if cycle != True: sum += cnt
    
    print(N - sum)





"""
사이클을 열심히 찾는 문제.

"""

"""
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

3
0
"""