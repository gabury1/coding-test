import heapq
import sys

input  = sys.stdin.readline

V, E = map(int, input().split())
t = int(input())
edge = [[] for _ in range(V+1)]
for _ in range(E) :
    start, end, w = map(int, input().split())
    edge[start].append((end, w)) # 도착지, 가중치


memo = [-1] * (V+1)
memo[t] = 0

q = []
heapq.heappush(q, (memo[t], t)) # 현재 가중치, 현재 노드

while q :
    now_w, now_node = heapq.heappop(q)

    if 0 <= memo[now_node] < now_w : continue
    for end, w in edge[now_node] :
        if now_w+w < memo[end] or memo[end] == -1 :
            memo[end] = now_w + w
            heapq.heappush(q, (memo[end], end))

for i in range(1, V+1) :
    if memo[i] == -1 : print("INF")
    else : print(memo[i])


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

"""