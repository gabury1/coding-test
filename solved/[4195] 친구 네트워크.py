# [4195] 친구 네트워크
# https://www.acmicpc.net/problem/4195
# 골드 2

import sys

input = sys.stdin.readline


T = int(input())

def find(name) :
    
    if union[name] == name :
        return name

    union[name] = find(union[name])
    return union[name]

for _ in range(T) :
    F = int(input())

    union = {}
    group_member = {}

    for i in range(F) : 
        a, b = input().split()
        if not a in union :
            union[a] = a
            group_member[a] = 1
        if not b in union :
            union[b] = b
            group_member[b] = 1
        
        a_root, b_root = find(a), find(b)
        if a_root != b_root :
            union[b_root] = union[a_root]
            group_member[a_root] += group_member[b_root]

        print(group_member[a_root])




        
"""
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty


2
3
4
2
2
4
"""