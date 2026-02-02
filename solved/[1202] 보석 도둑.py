# [1202] 보석 도둑
# https://www.acmicpc.net/problem/1202

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
jems = [tuple(map(int, input().split())) for _ in range(N)]
jems.sort(key=lambda x : x[1], reverse=True)
bags = [int(input()) for _ in range(K)]
bags.sort()
bags_full = [False] * K

sum = 0
for w, v in jems :
    for i in range(K) :
        bag_w = bags[i]
        if not bags_full[i] and w <= bag_w :
            sum += v
            bags_full[i] = True
            break

print(sum)


"""
3 2
1 65
5 23
2 99
10
2

2 1
5 10
100 100
11
"""

"""
가중치(가격) 을 기반으로 보석 내림차순 정렬,
무게를 기반으로 오름차순 주머니 정렬

후, 보석을 계속 넣어보다가, 보석을 전부 넣거나, 가방을 전부 사용했다면 출력해보면 되지 않을까?
그게 곧 최대값이 될 것 같다.

dfs로 돌려보자. 

"""