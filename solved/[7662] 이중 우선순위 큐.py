# [7662] 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
# 골드 4

import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    deleted_ids = {}
    maxq = []
    minq = []
    for id in range(N) :
        o, num = input().split()
        num = int(num)
        if o == "I" :
            heapq.heappush(maxq, (-num, id))
            heapq.heappush(minq, (num, id))
        elif o == 'D' :
            # 최대값 뽑기
            if num == 1:
                while maxq :
                    max_num, m_id = heapq.heappop(maxq)
                    # 이미 삭제된 원소일 경우 건너뛰기
                    if deleted_ids.get(m_id, False) : 
                        continue
                    else : 
                        deleted_ids[m_id] = True
                        break
            # 최소값 뽑기
            elif num == -1 :
                while minq :
                    min_num, m_id = heapq.heappop(minq)
                    if deleted_ids.get(m_id, False) : 
                        continue
                    else : 
                        deleted_ids[m_id] = True
                        break

        while maxq :
            max_num, id = heapq.heappop(maxq)
            if deleted_ids.get(id, False) : 
                continue
            else : 
                heapq.heappush(maxq, (max_num, id))
                break

        while minq :
            min_num, id = heapq.heappop(minq)
            if deleted_ids.get(id, False) : 
                continue
            else : 
                heapq.heappush(minq, (min_num, id))
                break

    if len(maxq) == 0 :
        print("EMPTY")
    else :
        print(-maxq[0][0], minq[0][0])
            



"""
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333

EMPTY
333 -45

"""