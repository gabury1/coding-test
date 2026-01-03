import heapq

N, E = map(int, input().split())

line = [[] for _ in range(N+1)]
memo = [[[-1] * 2 for _ in range(2)] for _ in range(N+1)] 

for _ in range(E) :
    s, e, w = map(int, input().split())
    line[s].append((w, e))
    line[e].append((w, s))

v1, v2 = map(int, input().split())

q = []
heapq.heappush(q, (0, 1, 1 if v1==1 else 0, 1 if v2==1 else 0)) # 음.. w, now, v1?, v2?


while q :
    now_w, now, is_v1, is_v2 = heapq.heappop(q)
    if 0 <= memo[now][is_v1][is_v2] < now_w : continue

    for weight, end in line[now] :
        # 다음에 들어갈 애가 2개의 정점을 통과했는지 확인
        next_is_v1 = 1 if end==v1 else is_v1
        next_is_v2 = 1 if end==v2 else is_v2
        
        if memo[end][next_is_v1][next_is_v2] == -1 or now_w + weight < memo[end][next_is_v1][next_is_v2] :
            memo[end][next_is_v1][next_is_v2] = now_w + weight
            heapq.heappush(q, (memo[end][next_is_v1][next_is_v2], end, next_is_v1, next_is_v2))

print(memo[N][1][1])


"""
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

7

======

4 6
1 2 3
2 3 3
3 3 1
1 3 5
2 3 5
1 3 4
2 3

-1
"""