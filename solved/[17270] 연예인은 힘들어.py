# [17270] 연예인은 힘들어
# https://www.acmicpc.net/problem/17270
# 골드 5

import sys
import heapq


def dijk(node : int) :
    global V, M, arr
    v = [float('inf') for _ in range(V+1)]
    v[node] = 0
    q = [(0, node)]
    heapq.heapify(q)

    while q :
        t, now = heapq.heappop(q)
        if v[now] < t :
            continue
        
        for time, next in arr[now] :
            if t+time < v[next] :
                v[next] = t+time
                heapq.heappush(q, (t+time, next))
    
    return v


input = sys.stdin.readline
V, M = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(M) :
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))
J, S = map(int, input().split())


j = dijk(J)
s = dijk(S)

# 합산거리, 지헌 시간, 번호
result = (float('inf'), 0, -1)
for idx, (jt, st) in enumerate(zip(j, s)) :
    if idx == J or idx == S :
        continue
    if jt == float('inf') or st == float('inf'):
        continue
    if st <= jt :
        continue

    if jt+st < result[0]:
        result = (jt+st, jt, idx)
    elif jt+st == result[0] :
        if jt < result[1] :
            result = (jt+st, jt, idx)
        elif jt == result[1] :
            if idx < result[2] :
                result = (jt+st, jt, idx)
            
print(result[2])

"""
8 10
1 2 2
2 6 3
2 7 2
1 3 1
3 7 2
4 7 5
5 6 2
5 7 2
7 8 2
5 8 2
3 6

1

2 1
1 2 1
1 2

"""
