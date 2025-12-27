def back_track(n, x, y) :
# n : 현재 단계, x : 현재 영역의 시작 x, y : 현재 영역의 시작 y
    if n == 0 : return 0

    offset = pow(2, n-1)
    block = offset * offset

    if c < x+offset and r < y+offset :
        return back_track(n-1, x, y)
    elif x + offset <= c and r < y+offset :
        return block*1 + back_track(n-1, x+offset, y)
    elif c < x+offset and y+offset <= r :
        return block*2 + back_track(n-1, x, y+offset)
    elif x + offset <= c and y+offset <= r :
        return block*3 + back_track(n-1, x+offset, y+offset)


N, r, c = map(int, input().split(" "))
result = back_track(N, 0, 0)
print(result)


"""
3 7 7
"""