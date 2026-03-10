# [1715] 카드 정렬하기
# https://www.acmicpc.net/problem/1715
# 골드 4
import sys
import heapq

input = sys.stdin.readline
N = int(input())
q = [int(input()) for _ in range(N)]
heapq.heapify(q)
sum = 0
while len(q) != 1 :
    #print(f"level : {sum}")
    #print(*q)
    c1 = heapq.heappop(q)
    c2 = heapq.heappop(q)
    #print(c1, c2)
    sum += c1 + c2
    heapq.heappush(q, c1+c2)
  
print(sum)



"""
3
10
20
40

100

6
30
20
10
20
30
40


100

"""
