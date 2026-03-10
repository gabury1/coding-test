

# 목표 X, 1, 5, 10, 25
X, A, B, C, D = map(int, input().split())

total = 0
result = (0, 0, 0, 0)

for q in range(D+1) :
    if X < q*25 : break
    for d in range(C+1) :
        if X < q*25 + d*10 : break
        for n in range(B+1) :
            if X <  q*25 + d*10 + n*5 : break
            cent = X - (q*25 + d*10 + n*5)
            if cent <= A :
                if total < sum((cent, n, d, q)) :
                    result = (cent, n, d, q)
                    total = sum(result)
                    

print(*result)


"""
12 5 3 1 2
2 2 0 0

100 5 100 100 1
"""