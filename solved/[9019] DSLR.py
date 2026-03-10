# [9019] DSLR
# https://www.acmicpc.net/problem/9019
# 골드 4

def D(num) :
    # num을 두배로, 만약 9999를 넘는다면 10000으로 나눈 나머지
    num *= 2
    if 9999 < num :
        num %= 10000
    return num

def S(num) :
    # num-1, 만약 0이라면 9999
    num -= 1
    if num == -1 :
        num = 9999
    return num
def L(num) :
    # 자릿수들을 하나씩 왼쪽으로
    left = num // 1000
    num = (num%1000)*10 + left
    return num

def R(num) :
    # 자릿수들을 하나씩 오른쪽으로
    right = num % 10
    num = right*1000 + (num//10)
    return num

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

#for i in range(10000) :
#    print(i)
#    print(D(i), S(i), L(i), R(i))

for t in range(T) :
    A, B = map(int, input().split())
    visited = [False] * 10000
    q = deque()
    q.append((A, ''))
    result = ''
    while q :
        now, letters = q.popleft()

        if now == B :
            result = letters
            break

        d, s, l, r = D(now), S(now), L(now), R(now)
        if not visited[d] : 
            q.append((d, letters+'D'))
            visited[d] = True
        if not visited[s] : 
            q.append((s, letters+'S'))
            visited[s] = True
        if not visited[l] : 
            q.append((l, letters+'L'))
            visited[l] = True
        if not visited[r] : 
            q.append((r, letters+'R'))
            visited[r] = True

    print(result)
        


"""

3
1234 3412
1000 1
1 16

LL
L
DDDD

"""


