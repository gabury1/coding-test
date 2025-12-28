import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 도시 수
M = int(input()) # 버스 수

# 버스 입력
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    s, e, w = map(int, input().split())
    graph[s].append((e, w))


# 시작, 도착
start, end = map(int, input().split())

# 최단거리 저장 배열
sp_arr = [float('inf')] * (N+1)
sp_arr[start] = 0

# 우선순위 큐
q = []
heapq.heappush(q, (0, start)) # 현재 도시, 현재까지 가중치

while q :
    dist, city = heapq.heappop(q)

    # 이미 처리된 노드 스킵
    if dist > sp_arr[city]:
        continue

    for e, w in graph[city] :
        new_dist = dist + w
        if new_dist < sp_arr[e] :
            sp_arr[e] = new_dist
            heapq.heappush(q, (new_dist, e))

print(sp_arr[end])



"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

"""