import sys

sys.setrecursionlimit(6**10)

def dfs(y, x) :
    global q, result

    if not (0 <= y < R and 0 <= x < C) or metric[y][x] in s :
        return 0

    s.add(metric[y][x])
    r = []
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
        r.append(dfs(y+dy, x+dx))

    s.remove(metric[y][x])
    
    m = max(r) + 1
    return m

R, C = map(int, input().split())
metric = [input() for _ in range(R)]
s = set()

print(dfs(0, 0))

"""
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
"""