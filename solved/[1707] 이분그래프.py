
def dfs(node, color) :
    
    if len(line[node]) == 0 : return True # 그래프 말단일때
    if vertex[node] != -1 : # 방문 전적이 있다면
        if color == vertex[node] : return True # 그래프가 이미 칠해져 있는데 같은 색이면
        else : return False # 그래프가 이미 칠해져있는데 다른 색이면

    vertex[node] = color
    for end in line[node] :
        if not dfs(end, abs(color-1)) : # False 면 걍 False 리턴
            return False
    return True
    

def test() :

    global line, vertex
    V, E = map(int, input().split())
    line = [[] for _ in range(V+1)]
    vertex = [-1 for _ in range(V+1)]
    
    for _ in range(E) :
        s, e = map(int, input().split())
        line[s].append(e)
    
    print("YES" if dfs(1, 0) else "NO")


    

K = int(input())

for _ in range(K) :
    test()



"""
입력:
첫째 줄: 테스트 케이스 개수 K
각 테스트 케이스:
  첫째 줄: 정점 V, 간선 E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 200,000)
  다음 E개 줄: 간선 정보 (u, v)

출력:
이분 그래프면 YES, 아니면 NO

예제 입력:
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

예제 출력:
YES
NO
"""