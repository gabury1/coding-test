# 그리디 (Greedy) 알고리즘

## 핵심 개념

**매 순간 최선의 선택을 하면 전체 최적해를 얻을 수 있는 알고리즘**

- 현재 상황에서 가장 좋은 것만 선택
- 한 번 선택하면 되돌리지 않음
- 빠르고 간단하지만, **항상 최적해를 보장하지는 않음**

## 언제 사용?

- ✅ **정렬** 후 순서대로 선택하는 문제
- ✅ 범위/구간 문제
- ✅ 최소/최대 개수 구하기
- ✅ **국소 최적 = 전역 최적**인 경우

⚠️ **주의**: 그리디가 항상 정답인지 증명 필요!

## 그리디 vs 다른 알고리즘

| 알고리즘 | 선택 방식 | 되돌림 | 시간복잡도 | 최적해 보장 |
|---------|----------|--------|-----------|-----------|
| 그리디 | 현재 최선 | ❌ | O(N log N) | ⚠️ 조건부 |
| 백트래킹 | 모든 경우 | ✅ | O(2^N ~ N!) | ✅ |
| DP | 모든 부분 문제 | - | O(N^2 ~ N^3) | ✅ |

## 실전 예제

### [1931] 회의실 배정 ⭐

```python
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# 핵심: 끝나는 시간 기준 정렬!
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
pre_end = 0

for start, end in meetings:
    if pre_end <= start:  # 겹치지 않으면
        count += 1
        pre_end = end

print(count)
```

**왜 그리디?**
- 끝나는 시간이 빠를수록 더 많은 회의 가능
- 가장 빨리 끝나는 회의를 선택 = 국소 최적
- 계속 반복 = 전역 최적 ✅

### ATM 대기 시간

```python
N = int(input())
times = list(map(int, input().split()))

# 시간이 짧은 사람부터
times.sort()

total = 0
accumulated = 0

for time in times:
    accumulated += time
    total += accumulated

print(total)
```

**왜 그리디?**
- 짧은 시간부터 처리하면 대기 시간 최소화
- [1, 2, 3] → 1 + (1+2) + (1+2+3) = 10
- [3, 2, 1] → 3 + (3+2) + (3+2+1) = 14

### 동전 거스름돈

```python
money = 1260
coins = [500, 100, 50, 10]

count = 0
for coin in coins:
    count += money // coin
    money %= coin

print(count)
```

**주의**: 동전이 배수 관계일 때만 그리디 가능!
- ✅ [500, 100, 50, 10] - 배수 관계
- ❌ [500, 400, 100] - 800원은 그리디로 불가능

## 그리디가 작동하는 조건

### 1. **탐욕 선택 속성 (Greedy Choice Property)**

현재 상황에서 최선의 선택이 전체 문제의 최적해로 이어짐

```python
# 회의실 배정
# 끝나는 시간이 빠른 회의 선택 = 최선
# → 남은 시간이 많음 → 더 많은 회의 가능
```

### 2. **최적 부분 구조 (Optimal Substructure)**

전체 문제의 최적해가 부분 문제의 최적해를 포함

```python
# ATM
# 전체 최소 대기 시간 = 각 단계에서 최소 선택
```

## 그리디 문제 패턴

### 패턴 1: 정렬 + 순차 선택

```python
# 1. 정렬
arr.sort(key=lambda x: 정렬기준)

# 2. 순서대로 선택
for item in arr:
    if 조건:
        선택
```

**예시**: 회의실 배정, ATM, 로프

### 패턴 2: 큰 것/작은 것부터

```python
# 최댓값 구하기 - 큰 것부터
arr.sort(reverse=True)

# 최솟값 구하기 - 작은 것부터
arr.sort()
```

**예시**: 동전 거스름돈, 보석 도둑

### 패턴 3: 양쪽에서 선택

```python
arr.sort()
left, right = 0, len(arr) - 1

while left <= right:
    if 조건:
        left += 1
    else:
        right -= 1
```

**예시**: 두 용액, 수들의 합

## 실수하기 쉬운 점

### 1. **정렬 기준 잘못 설정**

```python
# ❌ 시작 시간으로만 정렬
meetings.sort(key=lambda x: x[0])

# ❌ 끝나는 시간만
meetings.sort(key=lambda x: x[1])

# ✅ 끝나는 시간 우선, 같으면 시작 시간
meetings.sort(key=lambda x: (x[1], x[0]))
```

### 2. **그리디 가능 여부 판단 실패**

```python
# 동전 문제
coins = [500, 400, 100]
target = 800

# 그리디: 500 + 100 + 100 + 100 = 4개 ❌
# 정답: 400 + 400 = 2개 ✅

# → 이 경우 DP 사용해야 함!
```

### 3. **경계 조건**

```python
# 회의실 배정
if pre_end <= start:  # ✅ 같은 시간 허용
if pre_end < start:   # ❌ 같은 시간 불가

# 문제 조건 확인 필수!
```

## 그리디 vs 백트래킹

### 회의실 배정 예제

```python
# 백트래킹 (느림) - O(2^N)
def backtrack(idx, selected):
    if idx == N:
        return len(selected)

    # 선택 안함
    r1 = backtrack(idx + 1, selected)

    # 선택함 (겹치지 않으면)
    if can_select(idx, selected):
        selected.append(idx)
        r2 = backtrack(idx + 1, selected)
        selected.pop()
        return max(r1, r2)

    return r1

# 그리디 (빠름) - O(N log N)
meetings.sort(key=lambda x: (x[1], x[0]))
count = 0
pre_end = 0
for start, end in meetings:
    if pre_end <= start:
        count += 1
        pre_end = end
```

**백트래킹을 그리디로 바꾸는 힌트:**
- "범위", "구간", "시간" → 정렬 시도
- 정렬 후 앞에서부터 선택 가능? → 그리디

## 시간복잡도

일반적으로:
- **정렬**: O(N log N)
- **순회**: O(N)
- **전체**: O(N log N)

백트래킹(O(2^N))이나 DP(O(N^2))보다 훨씬 빠름!

## 그리디 판단 체크리스트

1. ✅ 정렬하면 규칙이 보이는가?
2. ✅ 국소 최적 선택이 전역 최적으로 이어지는가?
3. ✅ 반례가 없는가? (직접 찾아보기)
4. ✅ 선택을 되돌릴 필요가 없는가?

하나라도 No면 → DP, 백트래킹 고려

## 범위/구간 문제는 정렬부터!

**인사이트**:
> "범위", "구간", "시간"이 나오면 → 일단 정렬부터!

### 대표 유형:
1. **회의실 배정** - 끝나는 시간 정렬
2. **선 긋기** - 시작점 정렬
3. **로프** - 무게 정렬
4. **과제** - 마감일 정렬

자세한 내용: [`범위와 구간 문제는 정렬부터.md`](./범위와%20구간%20문제는%20정렬부터.md)

## 실전 팁

### 1. **정렬 기준 명확히**

```python
# 여러 조건 정렬
arr.sort(key=lambda x: (x[1], x[0]))  # 튜플 사용

# 내림차순
arr.sort(key=lambda x: -x[0])  # 음수
arr.sort(key=lambda x: x[0], reverse=True)  # reverse
```

### 2. **증명 해보기**

```python
# "왜 이게 최적일까?" 스스로 물어보기
# 반례 찾기
# 교환 논법 사용
```

### 3. **범위 문제 = 정렬**

```python
# 패턴 익히기
problems = ["회의실", "ATM", "로프", "선긋기"]
solution = "정렬 + 그리디"
```

## 체크리스트

- [ ] 정렬로 규칙을 찾았나?
- [ ] 그리디가 최적해를 보장하는가?
- [ ] 반례를 찾아봤는가?
- [ ] 정렬 기준이 명확한가?
- [ ] 경계 조건(같은 값)을 고려했나?
- [ ] 백트래킹/DP가 더 나은 건 아닌가?
