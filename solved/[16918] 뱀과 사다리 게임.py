from collections import deque
import sys
input = sys.stdin.readline

def loop() :
    while q :
        loc, cnt = q.popleft()
        if visited[loc] : continue
        visited[loc] = True 
        for i in range(1, 7) : # 1~6 조심
            if loc+i == 100 :
                return cnt+1
            elif mcs[loc + i] != 0 :
                q.append((mcs[loc+i], cnt+1))
            else  :
                q.append((loc+i, cnt+1))



# 사다리와 뱀
n, m = map(int, input().split(" "))
paths = [list(map(int, input().split(" "))) for _ in range(n + m)]
mcs = [0] * 101
visited = [False] * 101
for path in paths :
    a, b = path[0], path[1]
    mcs[a] = b # a로 가면 b로 이동함

q = deque()
q.append((1, 0)) # 현재 위치 , 현재 횟수

result = loop()
print(result)


    
    



"""
    특정 칸에 도착했을 경우 선택지 :
    1. 6칸 가기
    2. 6칸 내에 있는 사다리 / 뱀 타기

    BFS 로 한번 해보자.
    어느 칸에 도착하면 선택지들을 큐에 넣고,
    계속 돌리다보면 먼저 도착하는게 제일 빠른거겠지.

"""
"""
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

3
"""