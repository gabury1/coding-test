# [1005] ACM Craft
# https://www.acmicpc.net/problem/1005
# 골드 3

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    N, M = map(int, input().split())
    graph = [0] + [[] for _ in range(N)]
    indegrees = [0] + [0] * N
    times = [0] + list(map(int, input().split()))
    max_times = [-1] * (N+1)

    for _ in range(M) :
        a, b = map(int, input().split())
        graph[a].append(b)
        indegrees[b] += 1
    target = int(input())

    q = deque([(i, times[i]) for i in range(1, N+1) if indegrees[i] == 0])
    
    while q :
        now, time = q.popleft()
        
        if now == target :
            break

        for next in graph[now] :
            indegrees[next] -= 1
            max_times[next] = max(max_times[next], time+times[next])
            if indegrees[next] == 0:
                q.append((next, max_times[next]))


    print(time)

        


"""
위상정렬

테스트케이스
건물개수, 건설규칙개수
건설규칙
지어야할 건물

"""

"""
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7

120
39
"""