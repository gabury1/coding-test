# [16566] 카드 게임
# https://www.acmicpc.net/problem/16566
# 골드 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(6**10)
N, M, K = map(int, input().split())

cards = list(map(int, input().split()))
cards = {v:True for k, v in enumerate(cards)}
arr = list(map(int, input().split()))

union = [-1] + [-1] * N

for card in cards.keys() :
    union[card-1] = card

for i in range(1, N+1) :
        if union[i] == -1 :
            union[i] = i+1 if i != N else 1

def find(node) :
     if cards.get(union[node], False) : 
          return union[node]
     
     union[node] = find(union[node])
     return union[node]

for c in arr :
    choice = find(c)
    print(choice)
    cards[choice] = False



"""
할만..해보이는데?
걍 유니온 파인드네 ㅋㅋㅋㅋ

N = 4,000,000 주의



10 7 5
2 5 3 7 8 4 9
4 1 1 3 8

5
2
3
4
9

10 7 5
2 5 3 8 4 9
4 1 1 3 8

"""