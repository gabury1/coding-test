
N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
times = []
arr.sort(key = lambda x : (x[1], x[0]))

cnt=0
pre_end = -1
for start, end in arr :
    if pre_end <= start :
        pre_end = end
        times.append((start, end))
        cnt+=1

print(cnt)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4
"""