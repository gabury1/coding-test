import heapq

# 마을 개수,  도로 개수, 파티 마을
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    start, end, time = map(int, input().split())
    graph[start].append((end, time))


g = [[]]
for v in range(1, N+1) :
    q = [(0, v)]
    # 현재까지 거리를 담는 친구
    dist_arr = [float('inf') for _ in range(N+1)]
    
    while q :
        dis, village = heapq.heappop(q)

        # 지금까지보다도 거리가 길면 할 이유가 없음
        if dist_arr[village] < dis :
            continue
        
        dist_arr[village] = dis

        for v, t in graph[village] :
            if dis + t < dist_arr[v] :
                heapq.heappush(q, (dis + t, v))
    g.append(dist_arr)

result = 0
for i in range(1, N+1) :
    dis = g[X][i] + g[i][X]
    result = max(result, dis)
print(result)

"""
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

10
"""