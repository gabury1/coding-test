# [10830] 행렬 제곱
# https://www.acmicpc.net/problem/10830
# Gold 4

import sys

def met_mult(a, b) :

    left = m_mem[a]
    right = m_mem[b]

    r = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            sum = 0
            for k in range(N) :
                sum += left[i][k] * right[k][j] 
            r[i][j] = sum % 1000

    m_mem[a+b] = r


# m_mem 에다가 다 넣어놓고 돌릴거임
def dnq(b) :

    if m_mem.get(b) is not None :
        return b

    # 지수 분할
    if b % 2 == 1 :
        # 홀수 일때
        met_mult(dnq(b//2), dnq(b//2))
        met_mult(dnq(b-1), 1)

    else : 
        # 짝수 일때
        met_mult(dnq(b//2), dnq(b//2))
    
    return b



N, B = map(int, input().split())
m_original = [list(map(int, input().split())) for _ in range(N)]
m_mem = {}
m_mem[1] = m_mem[1] = [[m_original[i][j] % 1000 for j in range(N)] for i in range(N)]

dnq(B)

for i in range(N) :
    for j in range(N) :
        print(m_mem[B][i][j], end=" ")
    print("")



"""
크기가 N*N인 행렬 A가 주어졌을 때, A의 B제곱을 구하는 프로그램을 작성하시오.
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력:
- 첫째 줄: N (2 ≤ N ≤ 5), B (1 ≤ B ≤ 100,000,000,000)
- 둘째 줄부터 N개의 줄: 행렬의 각 원소 (1,000보다 작거나 같은 자연수 또는 0)

출력:
- A를 B제곱한 결과를 출력 (각 원소를 1000으로 나눈 나머지)

예제 입력 1:
2 5
1 2
3 4

예제 출력 1:
69 558
337 406
"""
