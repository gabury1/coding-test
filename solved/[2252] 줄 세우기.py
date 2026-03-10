# [2252] 줄 세우기
# https://www.acmicpc.net/problem/2252
# 골드 3

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
indegrees = [0] * (N+1)

for _ in range(M) :
    a, b = map(int, input().split())
    edges[a].append(b)
    indegrees[b] += 1

q = [node for node in range(1, N+1) if indegrees[node] == 0]
q = deque(q)

result = []
while q :
    node = q.popleft()
    result.append(node)

    for v in edges[node] :
        indegrees[v] -= 1
        if indegrees[v] == 0 :
            q.append(v)

print(*result)


"""
4 2
4 2
3 1

4 2 3 1

3 2
1 3
2 3

1 2 3

"""