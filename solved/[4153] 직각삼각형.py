
while True :
    a, b, c = [int(num) for num in input().split()]
    if a == 0 and b == 0 and c == 0 : break

    num = [a, b, c]
    num.sort(reverse=True)
    if pow(num[0], 2) == pow(num[1], 2) + pow(num[2], 2) : print("right")
    else : print("wrong")


"""
    간단한 문제였다.
    다만, num.sort() 사용법은 좀 알아두자.
"""
