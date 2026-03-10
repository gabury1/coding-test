# [5430] AC
# https://www.acmicpc.net/problem/5430
# 골드 5

import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    func = input()
    N = int(input())
    nums = input().replace("[", "").replace("]", "").split(",")
    nums = list(map(int, nums)) if 0 < N else []
    
    reversed = False
    error = False
    for c in func :
        if c == 'D' :
            if 0 < len(nums) :
                if not reversed :
                    del nums[0]
                else :
                    nums.pop()

            else :
                error = True
                
        elif c == 'R' :
            reversed = not reversed

    if reversed : nums.reverse()
    nums = str(nums).replace(" ", "")
    print(nums if not error else "error")

    


"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""