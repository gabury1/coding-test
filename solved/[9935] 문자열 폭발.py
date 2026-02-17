from collections import deque

def check() :
    global stack

    if bomb == ''.join(stack[-bomblen:]) :
        for _ in range(bomblen) :
            stack.pop()

string = input()
bomb = input()
bomblen = len(bomb)

stack = []

for c in string :
    stack.append(c)
    if c == bomb[-1:] :
        check()

if len(stack) == 0 : print("FRULA")
else : print("".join(stack))
        

"""
mirkovC4nizCC44
C4

mirkovniz


12ab112ab2ab
12ab

FRULA

"""