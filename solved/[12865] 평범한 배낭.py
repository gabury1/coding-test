
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = {0 : 0}

for w, v in arr :
    temp = {}
    for wkey, vitem in memo.items() :
        if wkey+w <= K :
            if wkey+w in memo :
                if memo[wkey+w] < memo[wkey] + v :
                    temp[wkey+w] = memo[wkey] + v
            else :
                temp[wkey+w] = memo[wkey] + v
    for k, v in temp.items() :
        memo[k] = v

print(max(memo.values()))
"""
4 7
6 13
4 8
3 6
5 12

14

5 1000
1 2
2 3
3 4
4 5
6 7



"""