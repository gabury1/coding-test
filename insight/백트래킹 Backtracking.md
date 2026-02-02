# 백트래킹 (Backtracking)

## 핵심 개념

**모든 경우의 수를 탐색하되, 조건을 만족하지 않으면 즉시 되돌아가서 탐색 중단**

- DFS + 가지치기(Pruning)
- 선택 → 탐색 → 선택 취소
- 완전 탐색보다 효율적

## 언제 사용?

- ✅ 모든 경우의 수를 확인해야 할 때
- ✅ 순열, 조합, 부분집합
- ✅ N-Queen, 스도쿠 같은 제약 조건 문제
- ✅ 최적해를 구해야 하는데 다른 방법이 없을 때

## 백트래킹 패턴

### 기본 구조

```python
def backtrack(depth, current_state):
    # 1. 종료 조건 (목표 달성)
    if depth == target:
        # 결과 저장
        return

    # 2. 모든 선택지 시도
    for choice in choices:
        # 3. 가지치기 (pruning) - 핵심!
        if not is_valid(choice):
            continue

        # 4. 선택
        make_choice(choice)

        # 5. 재귀 탐색
        backtrack(depth + 1, new_state)

        # 6. 선택 취소 (backtrack)
        undo_choice(choice)
```

## 실전 예제

### 1. 순열 (Permutation)

```python
def permutation(depth, path):
    if depth == N:
        result.append(path[:])  # 복사!
        return

    for i in range(N):
        if not used[i]:
            # 선택
            used[i] = True
            path.append(arr[i])

            # 탐색
            permutation(depth + 1, path)

            # 선택 취소
            path.pop()
            used[i] = False

N = 3
arr = [1, 2, 3]
used = [False] * N
result = []
permutation(0, [])
print(result)  # [[1,2,3], [1,3,2], [2,1,3], ...]
```

### 2. 조합 (Combination)

```python
def combination(depth, start, path):
    if depth == r:
        result.append(path[:])
        return

    for i in range(start, N):
        # 선택
        path.append(arr[i])

        # 탐색 (i+1부터 시작 - 중복 방지)
        combination(depth + 1, i + 1, path)

        # 선택 취소
        path.pop()

N, r = 4, 2
arr = [1, 2, 3, 4]
result = []
combination(0, 0, [])
print(result)  # [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

### 3. 회의실 배정 (백트래킹 버전)

```python
def backtrack(idx, selected):
    global max_count

    if idx == N:
        max_count = max(max_count, len(selected))
        return

    # 현재 회의 선택 안함
    backtrack(idx + 1, selected)

    # 현재 회의 선택
    start, end = meetings[idx]

    # 가지치기: 겹치는지 체크
    can_select = True
    for s, e in selected:
        if not (end <= s or e <= start):
            can_select = False
            break

    if can_select:
        selected.append((start, end))
        backtrack(idx + 1, selected)
        selected.pop()  # 백트래킹

max_count = 0
backtrack(0, [])
```

### 4. N-Queen

```python
def n_queen(row):
    if row == N:
        return 1  # 해 발견

    count = 0
    for col in range(N):
        # 가지치기: 놓을 수 있는지 체크
        if is_safe(row, col):
            # 선택
            board[row] = col

            # 탐색
            count += n_queen(row + 1)

            # 선택 취소 (board[row]는 다음 반복에서 덮어씀)

    return count

def is_safe(row, col):
    for prev_row in range(row):
        prev_col = board[prev_row]

        # 같은 열
        if prev_col == col:
            return False

        # 대각선
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True

N = 8
board = [-1] * N
print(n_queen(0))  # 92
```

## 핵심 포인트

### 1. **가지치기 (Pruning)** ⭐

```python
# ❌ 가지치기 없음 (완전 탐색)
def dfs(depth):
    if depth == N:
        if check_valid():  # 끝에서 체크
            count += 1
        return
    for choice in choices:
        make_choice()
        dfs(depth + 1)
        undo_choice()

# ✅ 가지치기 있음 (백트래킹)
def backtrack(depth):
    if depth == N:
        count += 1  # 이미 유효한 경로만 여기 도달
        return
    for choice in choices:
        if is_valid(choice):  # 미리 체크!
            make_choice()
            backtrack(depth + 1)
            undo_choice()
```

### 2. **선택 취소**

```python
# 리스트
path.append(x)
backtrack()
path.pop()  # 취소

# 집합
visited.add(x)
backtrack()
visited.remove(x)  # 취소

# 배열
board[i] = x
backtrack()
board[i] = 0  # 취소 (또는 다음 반복에서 덮어씀)
```

### 3. **깊은 복사 주의**

```python
# ❌ 잘못된 방법
if depth == N:
    result.append(path)  # 참조 복사! 나중에 path가 바뀌면 result도 바뀜

# ✅ 올바른 방법
if depth == N:
    result.append(path[:])  # 깊은 복사
    # 또는
    result.append(list(path))
    result.append(path.copy())
```

## 백트래킹 vs 완전탐색

| | 백트래킹 | 완전탐색 |
|---|---------|----------|
| 탐색 방법 | DFS + 가지치기 | 모든 경우 탐색 |
| 속도 | 빠름 | 느림 |
| 구현 | 복잡 | 간단 |
| 조건 체크 | 중간에 | 끝에서 |

```python
# 완전탐색: O(2^N) - 모든 경우 탐색
def brute_force(idx):
    if idx == N:
        if is_valid():  # 끝에서 체크
            process()
        return
    brute_force(idx + 1)  # 선택 안함
    select(idx)
    brute_force(idx + 1)  # 선택함
    deselect(idx)

# 백트래킹: 실제론 훨씬 적게 탐색
def backtrack(idx):
    if idx == N:
        process()  # 이미 유효한 것만 도달
        return

    if not is_valid():  # 중간에 체크
        return  # 가지치기!

    backtrack(idx + 1)  # 선택 안함
    select(idx)
    backtrack(idx + 1)  # 선택함
    deselect(idx)
```

## 시간복잡도

- **순열**: O(N!)
- **조합**: O(2^N)
- **부분집합**: O(2^N)
- **N-Queen**: O(N!) (가지치기로 실제론 훨씬 적음)

## 최적화 팁

### 1. **효율적인 가지치기**

```python
# 빨리 걸러낼수록 좋음
if obvious_invalid():  # 명백한 경우 먼저
    return

if complex_check():  # 복잡한 체크는 나중에
    return
```

### 2. **중복 제거**

```python
# 조합: start 인덱스 사용
def combination(depth, start):
    for i in range(start, N):  # start부터!
        backtrack(depth + 1, i + 1)

# 중복 순열 방지: 정렬 + 스킵
arr.sort()
for i in range(N):
    if i > 0 and arr[i] == arr[i-1]:
        continue  # 중복 스킵
```

### 3. **조기 종료**

```python
# 최댓값 갱신 후 가지치기
def backtrack(depth, current):
    global max_val

    # 현재까지 최대 + 남은 최선 < 현재 최대
    if current + remaining_best < max_val:
        return  # 더 탐색해도 의미 없음
```

## 회의실 배정 문제의 교훈

```python
# ❌ 백트래킹 (느림) - O(2^N)
def backtrack(idx):
    # 모든 경우의 수 탐색
    return max(선택함, 선택안함)

# ✅ 그리디 (빠름) - O(N log N)
meetings.sort(key=lambda x: (x[1], x[0]))
for start, end in meetings:
    if pre_end <= start:
        선택
```

**백트래킹은 만능이 아니다!**
- 정렬, 그리디로 풀 수 있으면 그게 훨씬 빠름
- 백트래킹은 **다른 방법이 없을 때** 최후의 수단

## Python 최적화 ⭐⭐⭐

백트래킹은 재귀가 깊고 호출이 많으니 Python 최적화가 특히 중요!

### 1. **재귀 호출 전에 체크** (호출 횟수 줄이기)

```python
# ❌ 재귀 안에서 체크 (불필요한 호출!)
def dfs(y, x):
    if not (0 <= y < R and 0 <= x < C): return 0  # 호출된 후에 체크
    if visited[y][x]: return 0
    ...
    for dy, dx in directions:
        dfs(y+dy, x+dx)  # 무조건 4번 호출

# ✅ 재귀 밖에서 체크 (호출 횟수 최소화!)
def dfs(y, x):
    ...
    for dy, dx in directions:
        ny, nx = y+dy, x+dx
        if not (0 <= ny < R and 0 <= nx < C): continue  # 호출 전 체크!
        if visited[ny][nx]: continue                     # 호출 전 체크!
        dfs(ny, nx)  # 유효한 경우만 호출
```

**파이썬에서 함수 호출은 비싼 연산!** 불필요한 호출 줄이는 게 핵심.

### 2. **리스트 생성 피하기 (global 활용)**

```python
# ❌ 매번 리스트 생성 + max 계산
def dfs(y, x):
    r = []
    for ...:
        r.append(dfs(...))
    return max(r) + 1

# ✅ global로 직접 업데이트
answer = 0
def dfs(y, x, count):
    global answer
    answer = max(answer, count)  # 직접 업데이트
    for ...:
        dfs(ny, nx, count + 1)
```

### 3. **재귀가 깊으면 반복문(stack)으로 변환**

```python
# ❌ 재귀 백트래킹 (깊은 재귀면 느림)
def dfs(y, x):
    ...
    dfs(ny, nx)
    ...  # 백트래킹

# ✅ 반복 stack (재귀 overhead 없음)
stack = set()
stack.add((y, x, state))
while stack:
    y, x, state = stack.pop()
    for ...:
        stack.add((ny, nx, new_state))
```

> **주의**: 반복 stack 백트래킹은 상태를 튜플로 관리해야 함 (선택 취소 불가)

### 4. **visited 체크: 배열 > set**

```python
# ✅ 배열 인덱스 (가장 빠름)
check = [False] * 26
check[ord(c) - ord('A')] = True

# ❌ set (해시 연산 overhead)
visited = set()
visited.add(c)
```

### Python 최적화 체크리스트
- [ ] 재귀 호출 전에 체크하고 있나? (불필요한 호출 줄이기)
- [ ] 리스트 생성을 피했나? (global 활용)
- [ ] 재귀가 깊은가? → 반복문 stack 고려
- [ ] visited를 배열로 구현했나?

---

## 비트마스킹 + 백트래킹

방문 상태를 **정수(mask)**로 표현하면 메모이제이션 가능!

```python
# 문자 A~Z를 비트로 표현
# A → 1 << 0 = 0b00...001
# B → 1 << 1 = 0b00...010
# C → 1 << 2 = 0b00...100

def dfs(y, x, mask):
    if (y, x, mask) in memo:
        return memo[(y, x, mask)]  # 캐시 반환

    idx = ord(grid[y][x]) - ord('A')

    # 방문 체크
    if mask & (1 << idx): return 0

    # 방문 추가
    new_mask = mask | (1 << idx)

    # 탐색
    result = 0
    for ny, nx in neighbors:
        result = max(result, dfs(ny, nx, new_mask))

    memo[(y, x, mask)] = result + 1
    return result + 1
```

**왜 비트마스킹?**
- set은 dict key로 쓸 수 없음 → 메모이제이션 불가
- 비트마스킹은 정수 → dict key 가능!
- ABC와 BAC 모두 같은 mask → 중복 탐색 제거!

---

## 체크리스트

- [ ] 가지치기 조건을 명확히 했나?
- [ ] 선택 취소를 제대로 했나?
- [ ] 결과 저장 시 깊은 복사했나?
- [ ] 중복 탐색을 방지했나?
- [ ] 더 효율적인 방법(그리디, DP)은 없나?
- [ ] Python 최적화: 재귀 호출 횟수 줄였나?
- [ ] Python 최적화: 리스트 생성 피했나?
- [ ] 메모이제이션 가능하면 비트마스킹 고려했나?
