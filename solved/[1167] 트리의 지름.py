# [1167] 트리의 지름
# https://www.acmicpc.net/problem/1167

import sys

sys.setrecursionlimit(6 ** 10)

def dfs(node) :
    global compared

    cand = []
    
    # 연결된 노드를 순회, 단 이미 방문한 노드는 방문하지 않음.
    # 연결된 노드가 이어진게 얼마나 길게 이어졌는지를 저장. (cand)
    for next, w in arr[node] :
        if not visited[next] :
            visited[node] = True
            l = dfs(next)
            visited[node] = False
            cand.append(l+w)
        
    if len(cand) == 0 : return 0
    # cand를 내림차순 정렬 후 자식 간의 트리 지름을 갱신
    elif 2 <= len(cand) :
        cand.sort(reverse=True)
        compared = max(compared, cand[0] + cand[1])
    
    # 쭉 이어진 노드가 트리지름이 될 수도 있음.
    compared = max(compared, cand[0])

    # 가장 긴 노드 길이 반환
    return cand[0]
            
    


input = sys.stdin.readline
N = int(input())

# (정점 번호, 간선 가중치)
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

compared = -1

for _ in range(N) :
    temp = list(map(int, input().split()))
    idx = 1
    while temp[idx * 2 - 1] != -1:
        arr[temp[0]].append((temp[idx * 2 - 1], temp[idx * 2]))
        idx+=1

dfs(1)
print(compared)


"""
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

11

2
1 2 2 -1
2 1 2 -1

2
"""