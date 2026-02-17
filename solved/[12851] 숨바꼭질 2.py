from collections import deque

N, K = map(int, input().split())
mem = [False] * (K*2 if N < K else N*2)
q = deque()
q.append((N, 0))

cnt = 0
r_sec = float("inf")

while(q) :
    n, sec = q.popleft()
    if n == K :
        # 종말 모드. 같은 sec의 K를 찾는다.
        cnt += 1
        r_sec = sec
        break
    mem[n] = True

    if n < K and not mem[n*2]:
        q.append((n*2, sec+1))
    if n < K and not mem[n+1]:
        q.append((n+1, sec+1))
    if 0 < n and not mem[n-1]: 
        q.append((n-1, sec+1))


while(q) :
    n, sec = q.popleft()
    if sec != r_sec :
        break
    if n == K :
        cnt+=1

print(r_sec)
print(cnt)

    



"""
5 17

4
2
"""