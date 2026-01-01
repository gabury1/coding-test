import heapq

N, K = map(int, input().split())

memo = [False] * (K * 2)
q = []
q.append((0, N))

result = []
while q :
    sec, now = heapq.heappop(q) 
    #print((sec, now))
    if now == K :
        result.append(sec)
        break
    if K < now :
        result.append(sec + now - K)
        continue

    if memo[now]:
        continue
    memo[now] = True

    if 0 <= now+1 < K*2 :
        heapq.heappush(q, (sec+1, now+1))  
    if 0 <= now-1 < K*2 :
        heapq.heappush(q, (sec+1, now-1))  
    if 0 <= now*2 < K*2 :
        heapq.heappush(q, (sec, now*2))

print(min(result))


"""
5 17
"""
