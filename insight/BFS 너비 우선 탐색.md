# BFS (너비 우선 탐색)

## 핵심 개념

**가까운 곳부터 차례대로 탐색**

- 큐(Queue) 사용
- 같은 거리에 있는 노드들을 먼저 탐색
- **최단 거리 보장** ⭐

## 언제 사용?

- ✅ **최단 거리** 문제 (가중치 없거나 모두 1)
- ✅ 최소 이동 횟수
- ✅ 레벨별 탐색
- ✅ 최소 시간/최소 비용 (가중치 동일)

## Python 구현 패턴

### 1. 기본 BFS

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

bfs(start)
```

### 2. 거리 추적 BFS

```python
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])  # (노드, 거리)
    visited = [False] * (N+1)
    visited[start] = True

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist  # 최단 거리 반환

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + 1))

    return -1  # 도달 불가
```

### 3. 그리드 BFS

```python
from collections import deque

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x, 0)])  # (y, x, 거리)
    visited = [[False]*M for _ in range(N)]
    visited[start_y][start_x] = True

    while queue:
        y, x, dist = queue.popleft()

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx

            # 범위 체크
            if not (0 <= ny < N and 0 <= nx < M):
                continue

            # 방문 체크
            if visited[ny][nx]:
                continue

            # 장애물 체크
            if grid[ny][nx] == 0:
                continue

            visited[ny][nx] = True
            queue.append((ny, nx, dist + 1))

    return -1
```

## 실전 예제

### [14940] 쉬운 최단거리

```python
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]

# 시작점 찾기
queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            queue.append((i, j, 0))
            result[i][j] = 0
        elif grid[i][j] == 0:
            result[i][j] = 0

# BFS
while queue:
    y, x, dist = queue.popleft()

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx

        if not (0 <= ny < n and 0 <= nx < m):
            continue

        if result[ny][nx] != -1:  # 이미 방문
            continue

        if grid[ny][nx] == 0:  # 갈 수 없음
            result[ny][nx] = 0
            continue

        result[ny][nx] = dist + 1
        queue.append((ny, nx, dist + 1))
```

### [7576] 토마토

```python
from collections import deque

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
unripe = 0

# 모든 익은 토마토를 큐에 추가
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j, 0))
        elif grid[i][j] == 0:
            unripe += 1

# BFS
max_days = 0
while queue:
    y, x, days = queue.popleft()
    max_days = max(max_days, days)

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == 0:
            grid[ny][nx] = 1
            unripe -= 1
            queue.append((ny, nx, days + 1))

print(max_days if unripe == 0 else -1)
```

## 핵심 포인트

### 1. **첫 도착 = 최단 거리**

```python
# BFS는 가까운 곳부터 탐색하므로
# 처음 도착한 경로가 무조건 최단!
if node == target:
    return dist  # 바로 리턴 가능
```

### 2. **방문 체크 타이밍**

```python
# ✅ 큐에 넣을 때 방문 체크 (추천)
if not visited[next]:
    visited[next] = True  # 여기서!
    queue.append(next)

# ❌ 큐에서 뺄 때 방문 체크 (비효율)
while queue:
    node = queue.popleft()
    if visited[node]:  # 중복 체크 발생
        continue
    visited[node] = True
```

### 3. **다중 시작점**

```python
# 여러 시작점이 있을 때 (토마토 문제)
queue = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:  # 시작점들
            queue.append((i, j, 0))

# 동시에 퍼져나감!
```

## 주의사항

### 1. **범위 체크 먼저**

```python
# ✅ 올바른 순서
if not (0 <= ny < N and 0 <= nx < M):
    continue
if visited[ny][nx]:
    continue

# ❌ 잘못된 순서 (IndexError 가능)
if visited[ny][nx] or not (0 <= ny < N):
    continue
```

### 2. **방문 체크와 조건 분리**

```python
# 명확하게 분리
if not (0 <= ny < N and 0 <= nx < M):
    continue  # 범위 체크

if visited[ny][nx]:
    continue  # 방문 체크

if grid[ny][nx] == 0:
    continue  # 조건 체크
```

### 3. **deque 사용 필수**

```python
# ❌ 일반 리스트 (느림)
queue = []
queue.append(x)
x = queue.pop(0)  # O(N) - 매우 느림!

# ✅ deque (빠름)
from collections import deque
queue = deque()
queue.append(x)
x = queue.popleft()  # O(1) - 빠름!
```

## BFS vs DFS

| | BFS | DFS |
|---|-----|-----|
| 자료구조 | 큐 (deque) | 스택 / 재귀 |
| 최단거리 | ✅ 보장 | ❌ 보장 안됨 |
| 메모리 | 많이 사용 | 적게 사용 |
| 구현 | 약간 복잡 | 간단 (재귀) |
| Python 안전성 | ✅ 재귀 제한 없음 | ⚠️ 재귀 깊이 제한 |

**선택 기준:**
- 최단 거리/최소 횟수 → **BFS** ⭐
- 모든 경로 탐색 → DFS
- Python 그리드 문제 → **BFS** (더 안전)

## 시간복잡도

- **그래프**: O(V + E) - V: 정점 수, E: 간선 수
- **그리드**: O(N × M) - 모든 칸 한 번씩 방문

## 최적화 팁

1. **목표 도달 시 즉시 종료**
   ```python
   if node == target:
       return dist  # 더 이상 탐색 불필요
   ```

2. **visited 배열 재활용**
   ```python
   # -1로 초기화하면 visited + dist 동시 저장
   dist = [-1] * (N+1)
   dist[start] = 0

   if dist[next] == -1:  # 미방문
       dist[next] = dist[node] + 1
   ```

3. **방향 벡터 활용**
   ```python
   # 4방향
   directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

   # 8방향
   directions = [(1,0), (1,1), (0,1), (-1,1),
                 (-1,0), (-1,-1), (0,-1), (1,-1)]
   ```

## 체크리스트

- [ ] `from collections import deque` 임포트했나?
- [ ] `deque` 사용하는가? (리스트 ❌)
- [ ] 큐에 넣을 때 방문 체크하는가?
- [ ] 범위 체크를 먼저 하는가?
- [ ] 최단 거리가 필요한 문제인가? (→ BFS 적합)
- [ ] 다중 시작점 고려했나?
