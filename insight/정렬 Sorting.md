# 정렬 (Sorting)

## 핵심 개념

**데이터를 특정 순서대로 배열하는 것**

- Python의 `sort()`는 Timsort - 매우 빠름 (O(N log N))
- 많은 알고리즘 문제의 **첫 단계**
- 정렬만 제대로 해도 문제가 쉬워짐

## Python 정렬 기본

### 1. **sort() - 리스트 자체를 정렬 (in-place)**

```python
arr = [3, 1, 4, 1, 5]
arr.sort()  # [1, 1, 3, 4, 5]
print(arr)  # [1, 1, 3, 4, 5]

arr.sort(reverse=True)  # 내림차순
print(arr)  # [5, 4, 3, 1, 1]
```

### 2. **sorted() - 새 리스트 반환**

```python
arr = [3, 1, 4, 1, 5]
result = sorted(arr)  # 새 리스트
print(arr)     # [3, 1, 4, 1, 5] (원본 유지)
print(result)  # [1, 1, 3, 4, 5]
```

### 3. **차이점**

| | sort() | sorted() |
|---|--------|----------|
| 반환값 | None | 새 리스트 |
| 원본 변경 | ✅ | ❌ |
| 사용 대상 | 리스트만 | 모든 iterable |

## lambda를 이용한 정렬

### 기본 사용법

```python
# ❌ 잘못된 사용 (옛날 Python 2 방식)
arr.sort(lambda a, b: b)  # 에러!

# ✅ key 파라미터 사용
arr.sort(key=lambda x: x[1])  # 두 번째 요소 기준
```

### 다양한 정렬 기준

```python
# 1. 단순 값
arr = [3, 1, 4, 1, 5]
arr.sort(key=lambda x: x)  # 오름차순
arr.sort(key=lambda x: -x)  # 내림차순

# 2. 튜플/리스트의 특정 요소
arr = [(3, 5), (1, 2), (4, 1)]
arr.sort(key=lambda x: x[1])  # 두 번째 요소 기준
# 결과: [(4, 1), (1, 2), (3, 5)]

# 3. 여러 조건 (튜플 반환)
arr = [(1, 5), (2, 3), (1, 2)]
arr.sort(key=lambda x: (x[0], x[1]))
# 결과: [(1, 2), (1, 5), (2, 3)]
# 첫 번째 요소 우선, 같으면 두 번째 요소

# 4. 복합 조건 (오름차순 + 내림차순)
arr = [(1, 5), (2, 3), (1, 2)]
arr.sort(key=lambda x: (x[0], -x[1]))
# 결과: [(1, 5), (1, 2), (2, 3)]
# 첫 번째 오름차순, 두 번째 내림차순

# 5. 길이, 알파벳 순 등
words = ["apple", "pie", "banana"]
words.sort(key=lambda x: len(x))
# 결과: ['pie', 'apple', 'banana']

words.sort(key=lambda x: (len(x), x))
# 결과: ['pie', 'apple', 'banana']
# 길이 우선, 같으면 알파벳 순
```

## 실전 예제

### [1931] 회의실 배정

```python
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 우선, 같으면 시작 시간
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
pre_end = 0
for start, end in meetings:
    if pre_end <= start:
        count += 1
        pre_end = end

print(count)
```

**핵심**: `(x[1], x[0])` - 튜플로 여러 조건 정렬

### 학생 성적 정렬

```python
students = [
    ("김철수", 85, 20),
    ("이영희", 90, 19),
    ("박민수", 85, 21),
]

# 점수 높은 순, 같으면 나이 낮은 순, 같으면 이름 순
students.sort(key=lambda x: (-x[1], x[2], x[0]))
```

### 문자열 정렬

```python
# 길이 짧은 순, 같으면 알파벳 순
words = ["abc", "a", "def", "ab"]
words.sort(key=lambda x: (len(x), x))
# 결과: ['a', 'ab', 'abc', 'def']
```

## 정렬 안정성 (Stable Sort)

Python의 `sort()`는 **안정 정렬**

```python
arr = [(1, 'a'), (2, 'b'), (1, 'c')]
arr.sort(key=lambda x: x[0])
# 결과: [(1, 'a'), (1, 'c'), (2, 'b')]
# 첫 번째 요소가 같을 때 원래 순서 유지
```

## 범위/구간 문제와 정렬

**핵심 인사이트**:
> "범위", "구간", "시간" 키워드 → 일단 정렬!

### 정렬 기준 선택

```python
# 1. 회의실 배정 - 끝나는 시간
meetings.sort(key=lambda x: (x[1], x[0]))

# 2. 선 긋기 - 시작점
lines.sort(key=lambda x: (x[0], x[1]))

# 3. 로프 - 무게
ropes.sort()

# 4. 작업 - 마감일, 점수
tasks.sort(key=lambda x: (x[1], -x[2]))
```

자세한 내용: [`범위와 구간 문제는 정렬부터.md`](./범위와%20구간%20문제는%20정렬부터.md)

## 정렬 + 그리디

대부분의 그리디 문제는 정렬이 필수!

```python
# 패턴
arr.sort(key=정렬기준)

for item in arr:
    if 조건:
        선택
```

## 정렬 시간복잡도

| 알고리즘 | 평균 | 최악 | 안정성 |
|---------|------|------|--------|
| Timsort (Python) | O(N log N) | O(N log N) | ✅ |
| Quick Sort | O(N log N) | O(N^2) | ❌ |
| Merge Sort | O(N log N) | O(N log N) | ✅ |
| Heap Sort | O(N log N) | O(N log N) | ❌ |

Python은 Timsort (Merge + Insertion)라서 **항상 O(N log N)**

## 주의사항

### 1. **lambda 사용법**

```python
# ❌ 잘못된 방법
arr.sort(lambda a, b: a - b)  # 옛날 방식 - 에러!

# ✅ 올바른 방법
arr.sort(key=lambda x: x)  # key 파라미터
```

### 2. **튜플 정렬**

```python
# 튜플은 앞에서부터 차례로 비교
arr = [(1, 3), (1, 2), (2, 1)]
arr.sort()
# 결과: [(1, 2), (1, 3), (2, 1)]
# 자동으로 (x[0], x[1]) 순서로 정렬됨
```

### 3. **문자열 정렬**

```python
# 사전순 (알파벳)
words = ["banana", "apple", "cherry"]
words.sort()
# 결과: ['apple', 'banana', 'cherry']

# 길이순
words.sort(key=lambda x: len(x))
# 결과: ['apple', 'banana', 'cherry']
```

### 4. **내림차순**

```python
# 방법 1: reverse=True
arr.sort(reverse=True)

# 방법 2: 음수 (숫자만)
arr.sort(key=lambda x: -x)

# 방법 3: sorted + reversed
arr = list(reversed(sorted(arr)))
```

## 정렬 활용 패턴

### 1. **이분 탐색 전처리**

```python
arr.sort()  # 이분 탐색은 정렬 필수
```

### 2. **투 포인터**

```python
arr.sort()  # 양쪽에서 접근
left, right = 0, len(arr) - 1
```

### 3. **중복 제거**

```python
arr.sort()
arr = list(set(arr))  # set + 정렬
```

### 4. **순위 매기기**

```python
arr.sort()
rank = {val: idx for idx, val in enumerate(arr)}
```

## 커스텀 비교 함수

복잡한 비교가 필요할 때:

```python
from functools import cmp_to_key

def compare(a, b):
    # a가 앞이면 -1
    # b가 앞이면 1
    # 같으면 0
    if a[0] != b[0]:
        return a[0] - b[0]
    return b[1] - a[1]

arr.sort(key=cmp_to_key(compare))
```

하지만 대부분은 `lambda`로 충분!

## 정렬 최적화

### 1. **제자리 정렬**

```python
# ✅ 메모리 절약
arr.sort()

# ❌ 메모리 2배
arr = sorted(arr)
```

### 2. **부분 정렬**

```python
# 상위 k개만 필요하면
import heapq
top_k = heapq.nsmallest(k, arr)  # O(N log k)
# vs
arr.sort()  # O(N log N)
top_k = arr[:k]
```

## 실전 팁

### 1. **정렬 기준 명확히**

```python
# 주석 달기
arr.sort(key=lambda x: (x[1], x[0]))  # (끝, 시작) 순
```

### 2. **경계 조건 확인**

```python
# 끝나는 시간이 같을 때 시작 시간도 고려?
meetings.sort(key=lambda x: (x[1], x[0]))  # 둘 다 고려
```

### 3. **정렬 후 규칙 찾기**

```python
arr.sort()
# 정렬 후 배열을 보면 패턴이 보임
# 그리디, 투 포인터 적용 가능
```

## 체크리스트

- [ ] `key=lambda x: ...` 형태로 썼나?
- [ ] 여러 조건은 튜플로 묶었나?
- [ ] 내림차순은 `-` 또는 `reverse=True`?
- [ ] 정렬 기준이 명확한가?
- [ ] 경계 조건 (같은 값) 고려했나?
- [ ] 정렬 후 어떤 알고리즘 쓸지 생각했나?
