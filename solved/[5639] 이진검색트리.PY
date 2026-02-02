import sys

sys.setrecursionlimit(6**10)

def devideRange(target, left, right) :
    
    for i in range(left, right+1) :
        if target < data[i] :
            return i
    return right+1


def tree(left, right) :
    if right < left :
        return

    if left == right :
        print(f"{data[left]}")
        return
    
    now = data[left]
    d = devideRange(now, left+1, right)
    #print(f"{(left+1, d-1)} {(d, right)}")
    tree(left+1, d-1)
    tree(d, right)
    print(f"{now}")
    

data = sys.stdin.read().split()
#data = [50, 30, 24, 5, 28, 45, 98, 52, 60]
data = list(map(int, data))

tree(0, len(data)-1)

