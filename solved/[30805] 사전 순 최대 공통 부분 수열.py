
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a, b= A, B
result = []
while len(a) != 0 and len(b) != 0 :
    am, bm = max(a), max(b)
    ai, bi = a.index(am), b.index(bm)
    if am == bm :
        result.append(am)
        a = a[ai+1:]
        b = b[bi+1:]
    
    elif am > bm :
        a.remove(am)
    
    elif am < bm :
        b.remove(bm)

print(len(result))
if 0<len(result) : print(*result)

"""
4
1 9 7 3
5
1 8 7 5 3

2
7 3

 
6
4 6 7 4 2 7
6
7 7 6 4 4 2

4
5 6 7 8
6
1 1 2 2 3 1


1
1
1
2
"""