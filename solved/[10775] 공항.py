# [10775] 공항
# https://www.acmicpc.net/problem/10775
# 골드 2



import sys

sys.setrecursionlimit(6**10)
input = sys.stdin.readline

G = int(input())
P = int(input())

union = [i for i in range(G+1)]

def find(node) :
    if node == 0 :
        return -1

    if union[node] == node :
        union[node] = node-1
        return node
    
    union[node] = find(union[node])
    return union[node]

cnt = 0
for i in range(P) :
    g = int(input())
    gate = find(g)
    if gate == -1 :
        break
    cnt+=1

print(cnt)



"""
4
6
2
2
3
3
4
4

3


4
3
4
1
1

2
"""