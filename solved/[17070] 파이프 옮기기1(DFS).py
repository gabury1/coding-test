import sys
sys.setrecursionlimit(6**10)


def is_success(r, c) :
    # 성공여부 체크용
    return True if r==N-1 and c==N-1 else False
def is_failed(r, c) :
    if not (0<=r<N and 0<=c<N) : return True
    if mtx[r][c] == 1 : return True

def pipe_check(r, c, type) :
    """
        type = 0 : 가로 방향 파이프
        type = 1 : 대각선 방향 파이프
        type = 2 : 세로 방향 파이프
    """
    fail_flag = False # 중간에 벽지가 있으면
    success_flag = False # 마지막에 도달했다면
    match type :
        case 0 : 
            for i in range(2) :
                if is_failed(r, c+i) :
                    return (True, False)
                if is_success(r, c+i) :
                    success_flag = True
        case 1 :
            for i in range(2) :
                for j in range(2) :
                    if is_failed(r+i, c+j) :
                        return (True, False)
                    if is_success(r+i, c+j) :
                        success_flag = True

        case 2 : 
            for i in range(2) :
                if is_failed(r+i, c) :
                    return (True, False)
                if is_success(r+i, c) :
                    success_flag = True
    
    return (fail_flag, success_flag)

def dp(r, c, t) :

    if memo[r][c][t] != -1 :
        return memo[r][c][t]
    
    fail_flag, success_flag = pipe_check(r, c, t)
    if fail_flag :
        memo[r][c][t] = 0
        return 0
    if success_flag :
        memo[r][c][t] = 1
        return 1

    success_cnt = 0
    memo[r][c][t] = 0
    if t == 0 :
        success_cnt += dp(r, c+1, 0)
        success_cnt += dp(r, c+1, 1)
    if t == 1 :
        success_cnt += dp(r+1, c+1, 1)
        success_cnt += dp(r+1, c+1, 0)
        success_cnt += dp(r+1, c+1, 2)
    if t == 2 :
        success_cnt += dp(r+1, c, 2)
        success_cnt += dp(r+1, c, 1)

    memo[r][c][t] = success_cnt
    return success_cnt

N = int(input())
mtx = [list(map(int, input().split())) for _ in range(N)]
memo = [[[-1] * 3 for _ in range(N+1) ] for _ in range(N+1)]

print(dp(0,0,0))
    
"""
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

3
0 0 0
0 0 0
0 0 0
"""

"""
최초 시도, 구현 + DP로 풀 생각.
1. memo[r,c,t] ((r,c)의 위치에서 t 형태일때) 답으로 가는 가짓 수는 정해져있다고 가정.

생각한게 맞았다! 하지만 문제를 제대로 이해하지 못해 애먹었다...
바텀업도 해봐야지 !
"""