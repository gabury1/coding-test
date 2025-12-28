# 다익스트라 (Dijkstra) 알고리즘

## 핵심 개념

**하나의 시작점에서 다른 모든 정점까지의 최단 경로를 구하는 알고리즘**

- 우선순위 큐(힙) 사용
- **양의 가중치**만 가능 (음수 가중치 ❌)
- 그리디 + BFS의 결합

## 언제 사용?

- ✅ **가중치가 있는** 최단 경로
- ✅ 한 정점에서 모든 정점까지의 최단 거리
- ✅ 특정 두 정점 간 최단 경로
- ✅ 양의 가중치만 존재

❌ 음수 가중치 있으면 → 벨만-포드 사용

## Python 구현 (표준 템플릿)

```python
import heapq
import sys
input = sys.stdin.readline

# 입력
N = int(input())  # 노드 수
M = int(input())  # 간선 수

# 인접 리스트
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))  # (도착지, 비용)

start, end = map(int, input().split())

# 다익스트라
def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0

    heap = [(0, start)]  # (거리, 노드)

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        # 이미 처리된 노드 스킵 (핵심!)
        if cur_dist > dist[cur_node]:
            continue

        # 인접 노드 탐색
        for next_node, weight in graph[cur_node]:
            new_dist = cur_dist + weight

            # 더 짧은 경로 발견
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist

result = dijkstra(start)
print(result[end])
```

## 핵심 포인트

### 1. **우선순위 큐 (heapq) 사용** ⭐

```python
import heapq

heap = []
heapq.heappush(heap, (거리, 노드))  # 거리가 작은 것부터
dist, node = heapq.heappop(heap)
```

**왜 우선순위 큐?**
- 가장 가까운 노드부터 처리해야 최적해 보장
- 일반 큐(BFS)로는 불가능 (가중치가 다르므로)

### 2. **중복 처리 방지** ⭐⭐

```python
while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    # 핵심: 이미 더 짧은 경로로 처리됨
    if cur_dist > dist[cur_node]:
        continue  # 스킵!

    # 인접 노드 탐색...
```

**없으면 무슨 일이?**
- 같은 노드를 여러 번 처리 → 시간 초과
- 메모리 초과

### 3. **거리 갱신**

```python
for next_node, weight in graph[cur_node]:
    new_dist = cur_dist + weight

    if new_dist < dist[next_node]:
        dist[next_node] = new_dist  # 갱신
        heapq.heappush(heap, (new_dist, next_node))
```

**포인트:**
- 더 짧은 경로를 발견하면 즉시 갱신
- 큐에 다시 추가 (나중에 스킵됨)

## 실전 예제

### [1916] 최소 비용 구하기

```python
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 인접 리스트 (메모리 효율적!)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

# 다익스트라
dist = [float('inf')] * (N+1)
dist[start] = 0

heap = [(0, start)]

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    # 중복 처리 방지
    if cur_dist > dist[cur_node]:
        continue

    for next_node, weight in graph[cur_node]:
        new_dist = cur_dist + weight

        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heapq.heappush(heap, (new_dist, next_node))

print(dist[end])
```

## 다익스트라 vs BFS

| | 다익스트라 | BFS |
|---|-----------|-----|
| 가중치 | 양의 가중치 | 없거나 모두 1 |
| 자료구조 | 우선순위 큐 (힙) | 일반 큐 (deque) |
| 시간복잡도 | O(E log V) | O(V + E) |
| 최단거리 | ✅ | ✅ (가중치 1일 때만) |

**선택 기준:**
- 가중치가 모두 같으면 → BFS (더 빠름)
- 가중치가 다르면 → 다익스트라

## 그래프 표현 방식

### 1. 인접 행렬 (메모리 초과 주의!)

```python
# ❌ N이 크면 메모리 초과
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s][e] = w

# 사용
for next_node in range(1, N+1):
    weight = graph[cur_node][next_node]
    if weight != 0:
        # 처리
```

**문제점:**
- N=1000이면 1,000,000개 배열 → 메모리 초과
- M=100개만 사용해도 나머지는 낭비

### 2. 인접 리스트 (추천!) ✅

```python
# ✅ 메모리 효율적
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# 사용
for next_node, weight in graph[cur_node]:
    # 처리
```

**장점:**
- 실제 간선 개수만큼만 메모리 사용
- 탐색도 빠름 (연결된 것만 확인)

## 주의사항

### 1. **heapq는 최소 힙**

```python
# ✅ (거리, 노드) - 거리가 작은 것부터
heapq.heappush(heap, (dist, node))

# ❌ (노드, 거리) - 노드 번호 순서대로 (잘못됨!)
heapq.heappush(heap, (node, dist))
```

### 2. **초기값 설정**

```python
# ✅ 무한대로 초기화
dist = [float('inf')] * (N+1)
dist[start] = 0

# ❌ 큰 수로 초기화 (오버플로우 가능)
dist = [99999999] * (N+1)
dist = [1 << 32 - 1] * (N+1)  # 연산자 우선순위 주의!
```

### 3. **방향 그래프 vs 무방향 그래프**

```python
# 방향 그래프
graph[s].append((e, w))  # s → e만

# 무방향 그래프
graph[s].append((e, w))  # s → e
graph[e].append((s, w))  # e → s (양방향)
```

### 4. **음수 가중치**

```python
# ❌ 다익스트라는 음수 가중치 처리 불가
# 음수 사이클이 있으면 최단 경로가 무한히 짧아짐

# 음수 가중치 있으면 → 벨만-포드 사용
```

## 알고리즘 동작 원리

```
그래프:
1 --(2)-- 2
|         |
(3)      (1)
|         |
3 --(4)-- 4

시작점: 1

1. dist = [∞, 0, ∞, ∞, ∞]
   heap = [(0, 1)]

2. pop (0, 1)
   → 2: dist[2] = 2, heap = [(2, 2)]
   → 3: dist[3] = 3, heap = [(2, 2), (3, 3)]

3. pop (2, 2)
   → 4: dist[4] = 3, heap = [(3, 3), (3, 4)]

4. pop (3, 3)
   → 4: 3 + 4 = 7 > dist[4] = 3 (갱신 안함)

5. pop (3, 4)
   → 완료

최종: dist = [∞, 0, 2, 3, 3]
```

## 최적화

### 1. **목표 지점 도달 시 종료**

```python
while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    # 목표 도달
    if cur_node == end:
        return cur_dist  # 즉시 종료

    if cur_dist > dist[cur_node]:
        continue
    # ...
```

### 2. **양방향 다익스트라**

```python
# 시작점과 끝점에서 동시에 탐색
# 만나는 지점에서 종료
# 약 2배 빠름
```

## 시간복잡도

- **O(E log V)**
  - E: 간선 수
  - V: 정점 수
  - log V: 힙 연산

**비교:**
- 플로이드-워셜: O(V^3) - 모든 쌍
- 벨만-포드: O(VE) - 음수 가중치
- 다익스트라: O(E log V) - 단일 시작점

## 사이클이 있어도 되나?

✅ **네! 양의 가중치 사이클은 문제없음**

```python
# 사이클 있어도 OK
1 → 2 → 3
↑       ↓
←←←←←←←←

# dist 배열로 이미 처리된 노드 스킵하므로
# 무한 루프 안 생김
```

❌ **음의 가중치 사이클은 불가**
- 계속 돌면 거리가 무한히 짧아짐

## BFS vs 다익스트라 비교

```python
# BFS (가중치 1)
from collections import deque
queue = deque([start])
while queue:
    node = queue.popleft()  # FIFO
    for next in graph[node]:
        queue.append(next)

# 다익스트라 (가중치 다양)
import heapq
heap = [(0, start)]
while heap:
    dist, node = heapq.heappop(heap)  # 최소 거리 먼저
    for next, w in graph[node]:
        heapq.heappush(heap, (dist+w, next))
```

## 실전 팁

### 1. **인접 리스트 사용**

```python
# 메모리 초과 방지
graph = [[] for _ in range(N+1)]
```

### 2. **중복 처리 방지 필수**

```python
if cur_dist > dist[cur_node]:
    continue  # 이거 없으면 시간/메모리 초과!
```

### 3. **heapq 튜플 순서**

```python
heapq.heappush(heap, (거리, 노드))  # 거리가 먼저!
```

## 체크리스트

- [ ] `import heapq` 했나?
- [ ] 인접 리스트로 구현했나?
- [ ] `dist` 배열 `float('inf')`로 초기화했나?
- [ ] 힙에 `(거리, 노드)` 순서로 넣었나?
- [ ] 중복 처리 방지 (`if cur_dist > dist[cur_node]`) 했나?
- [ ] 더 짧은 경로 발견 시 `dist` 갱신했나?
- [ ] 음수 가중치는 없나?
- [ ] 방향성 확인했나? (방향/무방향)
