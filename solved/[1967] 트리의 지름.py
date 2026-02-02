# [1967] 트리의 지름
# https://www.acmicpc.net/problem/1967

import sys

sys.setrecursionlimit(6**10)

result = 0

def dfs(node) :

    global result
    if len(child_node[node]) == 0 : return 0

    child_dis = []
    for n, w in child_node[node] :
        d = dfs(n) + w
        child_dis.append(d)

    child_dis.sort(reverse=True)
    if 2 <= len(child_dis) :
        dis = child_dis[0] + child_dis[1]
        if result < dis :
            result = dis

    return child_dis[0]
    

N = int(input()) # 노드 개수

child_node = [[] for _ in range(N+1)]

# 각 노드의 연결 위치
for _ in range(N-1) :
    parents, child, w = map(int, input().split())
    child_node[parents].append((child, w)) # 자식 노드 , 가중치

d = dfs(1)
print(result if result > d else d)

"""
타고 들어가면서, 양 정점의 가장 끝이 큰 애들로 max해서 return 하자.
"""

"""
트리의 지름: 트리에서 가장 먼 두 정점 사이의 거리

예제:
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10


답: 45
"""
