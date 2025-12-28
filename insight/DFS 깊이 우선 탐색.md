# DFS (깊이 우선 탐색)

## 핵심 개념

**한 방향으로 끝까지 탐색한 후, 다시 돌아와서 다른 방향 탐색**

- 스택(Stack) 또는 재귀(Recursion) 사용
- 깊이를 우선으로 탐색
- 백트래킹과 함께 자주 사용

## 언제 사용?

- ✅ 모든 경로를 탐색해야 할 때
- ✅ 경로의 특징을 저장해야 할 때
- ✅ 순열/조합 문제
- ✅ 사이클 탐지
- ✅ 연결 요소 찾기

## Python 구현 패턴

### 1. 재귀 방식 (추천)

```python
def dfs(node):
    # 종료 조건
    if 종료조건:
        return

    # 방문 처리
    visited[node] = True

    # 인접 노드 탐색
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

# 시작
visited = [False] * (N+1)
dfs(start)
```

### 2. 스택 방식

```python
stack = [start]
visited = [False] * (N+1)
visited[start] = True

while stack:
    node = stack.pop()

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
```

### 3. 그리드 DFS (2차원 배열)

```python
def dfs(y, x):
    # 범위 체크
    if not (0 <= y < n and 0 <= x < m):
        return

    # 방문 체크
    if visited[y][x]:
        return

    visited[y][x] = True

    # 상하좌우 탐색
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dfs(y + dy, x + dx)
```

## 실전 예제

### [10026] 적록색약

```python
import sys
sys.setrecursionlimit(10001)  # 재귀 깊이 설정

def dfs(color, y, x):
    if not (0 <= y < N and 0 <= x < N):
        return
    if visited[y][x] or grid[y][x] != color:
        return

    visited[y][x] = True

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dfs(color, y + dy, x + dx)

# 일반인
visited = [[False]*N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(grid[i][j], i, j)
            count += 1
```

## 주의사항

### 1. **재귀 깊이 제한**

```python
import sys
sys.setrecursionlimit(10001)  # 필수!
```

- Python 기본 재귀 깊이: 1000
- 그리드 문제 (N=100): 최대 10,000 필요
- 너무 크게 설정 금지: `6**10` 같은 건 과도함

### 2. **방문 체크 타이밍**

```python
# ❌ 잘못된 방법
def dfs(node):
    if visited[node]:
        return
    visited[node] = True  # 늦게 체크하면 중복 호출

# ✅ 올바른 방법
def dfs(node):
    visited[node] = True  # 먼저 체크
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
```

### 3. **범위 체크 순서**

```python
# ❌ 잘못된 순서
if grid[y][x] != 'R' or not (0 <= y < N):
    # IndexError 발생 가능!

# ✅ 올바른 순서
if not (0 <= y < N and 0 <= x < M) or grid[y][x] != 'R':
    return
```

## DFS vs BFS

| | DFS | BFS |
|---|-----|-----|
| 자료구조 | 스택 / 재귀 | 큐 |
| 시간복잡도 | O(V + E) | O(V + E) |
| 공간복잡도 | O(H) (높이) | O(W) (너비) |
| 최단경로 | ❌ | ✅ |
| 모든경로 | ✅ | ❌ |
| 구현 | 간단 (재귀) | 약간 복잡 |

**선택 기준:**
- 최단 거리 필요 → BFS
- 모든 경로 탐색 → DFS
- 경로 특징 저장 → DFS
- Python에서 안전성 → BFS (재귀 제한 없음)

## 시간복잡도

- **그래프**: O(V + E) - V: 정점 수, E: 간선 수
- **그리드**: O(N × M) - 모든 칸 방문

## 최적화 팁

1. **불필요한 탐색 줄이기**
   ```python
   # 목표 발견 시 즉시 종료
   if node == target:
       return True
   ```

2. **조기 종료**
   ```python
   # 가지치기
   if 불가능한_조건:
       return
   ```

3. **Python에서는 BFS 고려**
   - 재귀 깊이 걱정 없음
   - 더 안정적

## 체크리스트

- [ ] `sys.setrecursionlimit()` 설정했나?
- [ ] 종료 조건 명확한가?
- [ ] 범위 체크 먼저 하는가?
- [ ] 방문 체크 제대로 하는가?
- [ ] 최단 거리 문제는 아닌가? (→ BFS)
