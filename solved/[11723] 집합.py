import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        s.add(int(cmd[1]))
    elif op == "remove":
        s.discard(int(cmd[1]))
    elif op == "check":
        print(1 if int(cmd[1]) in s else 0)
    elif op == "toggle":
        num = int(cmd[1])
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif op == "all":
        s = set(range(1, 21))
    elif op == "empty":
        s.clear()

        """
            import sys
            input = sys.stdin.readline
        
            입력 속도를 빠르게 해준다. 무조건 기억하자.
            
        """