# SQL 기본 정리

## 핵심 개념

**데이터베이스에서 데이터를 조회/조작하는 언어**

- SQL 실행 순서: `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`
- 작성 순서와 실행 순서가 다름! (SELECT가 먼저 써지지만 나중에 실행됨)

---

## SELECT 기본

```sql
SELECT 컬럼1, 컬럼2       -- 가져올 컬럼
FROM 테이블명              -- 어떤 테이블에서
WHERE 조건                 -- 필터링
ORDER BY 컬럼 ASC/DESC    -- 정렬
LIMIT 10;                  -- 개수 제한
```

```sql
-- 전체 컬럼
SELECT * FROM employees;

-- 특정 컬럼
SELECT name, salary FROM employees;

-- 별칭 (alias)
SELECT name AS 이름, salary AS 급여 FROM employees;

-- 중복 제거
SELECT DISTINCT department FROM employees;
```

---

## WHERE 조건

```sql
-- 비교 연산자
WHERE salary > 3000
WHERE salary >= 3000
WHERE salary = 3000
WHERE salary != 3000  -- 또는 <>

-- 범위
WHERE salary BETWEEN 2000 AND 5000

-- 목록
WHERE department IN ('개발', '마케팅', '디자인')
WHERE department NOT IN ('총무')

-- 문자열 패턴 (LIKE)
WHERE name LIKE '김%'     -- 김으로 시작
WHERE name LIKE '%수'     -- 수로 끝
WHERE name LIKE '%민%'    -- 민 포함
WHERE name LIKE '김_수'   -- 김?수 (글자 하나)

-- NULL 처리
WHERE phone IS NULL
WHERE phone IS NOT NULL

-- 복합 조건
WHERE department = '개발' AND salary > 3000
WHERE department = '개발' OR department = '마케팅'
WHERE NOT (salary < 2000)
```

---

## GROUP BY / HAVING

```sql
-- 부서별 평균 급여
SELECT department, AVG(salary) AS 평균급여
FROM employees
GROUP BY department;

-- HAVING: GROUP BY 결과 필터링 (WHERE는 그룹화 전, HAVING은 그룹화 후)
SELECT department, AVG(salary) AS 평균급여
FROM employees
GROUP BY department
HAVING AVG(salary) > 3000;
```

| | WHERE | HAVING |
|---|-------|--------|
| 적용 시점 | 그룹화 전 | 그룹화 후 |
| 집계함수 사용 | ❌ | ✅ |
| 사용 위치 | GROUP BY 앞 | GROUP BY 뒤 |

---

## 집계 함수

```sql
SELECT
    COUNT(*)            AS 전체행수,
    COUNT(phone)        AS 전화번호있는행수,  -- NULL 제외
    SUM(salary)         AS 급여합계,
    AVG(salary)         AS 평균급여,
    MAX(salary)         AS 최고급여,
    MIN(salary)         AS 최저급여
FROM employees;
```

> COUNT(\*)는 NULL 포함, COUNT(컬럼)은 NULL 제외!

---

## JOIN

```sql
-- INNER JOIN: 양쪽 모두 있는 것만
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN: 왼쪽 기준 (오른쪽 없으면 NULL)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- RIGHT JOIN: 오른쪽 기준 (왼쪽 없으면 NULL)
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;

-- FULL OUTER JOIN: 양쪽 모두 포함
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.id;
```

```
INNER JOIN:   A ∩ B
LEFT JOIN:    A 전체 (B 없으면 NULL)
RIGHT JOIN:   B 전체 (A 없으면 NULL)
FULL JOIN:    A ∪ B
```

---

## 서브쿼리 (Subquery)

```sql
-- WHERE 안에 서브쿼리
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- FROM 안에 서브쿼리 (인라인 뷰)
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_avg
WHERE avg_salary > 3000;

-- IN과 함께
SELECT name
FROM employees
WHERE dept_id IN (
    SELECT id FROM departments WHERE location = '서울'
);

-- EXISTS
SELECT name
FROM employees e
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.emp_id = e.id
);
```

---

## NULL 처리

```sql
-- NULL은 =로 비교 불가, IS NULL / IS NOT NULL 사용
WHERE phone IS NULL      -- ✅
WHERE phone = NULL       -- ❌ 항상 false

-- COALESCE: NULL이면 대체값
SELECT name, COALESCE(phone, '번호없음') AS 전화번호
FROM employees;

-- IFNULL (MySQL)
SELECT IFNULL(phone, '번호없음') FROM employees;

-- NULL 포함 연산 주의
SELECT NULL + 1;   -- NULL
SELECT NULL = NULL;  -- NULL (true가 아님!)
```

---

## 윈도우 함수 (Window Function)

```sql
-- 전체 평균과 개인 급여 동시에
SELECT
    name,
    salary,
    AVG(salary) OVER() AS 전체평균,
    AVG(salary) OVER(PARTITION BY department) AS 부서평균
FROM employees;

-- 순위
SELECT
    name,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS 순위,        -- 동점 건너뜀 (1,1,3)
    DENSE_RANK() OVER(ORDER BY salary DESC) AS 밀집순위, -- 동점 안건너뜀 (1,1,2)
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS 행번호   -- 무조건 고유 (1,2,3)
FROM employees;

-- 누적합
SELECT
    name,
    salary,
    SUM(salary) OVER(ORDER BY name) AS 누적급여
FROM employees;
```

---

## ORDER BY

```sql
-- 오름차순 (기본값)
ORDER BY salary ASC
ORDER BY salary          -- ASC 생략 가능

-- 내림차순
ORDER BY salary DESC

-- 여러 조건 (salary 내림차순, 같으면 name 오름차순)
ORDER BY salary DESC, name ASC

-- NULL 위치 지정 (DB마다 다름)
ORDER BY salary DESC NULLS LAST   -- NULL을 맨 뒤로
```

---

## 문자열 함수

```sql
LENGTH('hello')          -- 5
UPPER('hello')           -- 'HELLO'
LOWER('HELLO')           -- 'hello'
TRIM('  hello  ')        -- 'hello'
SUBSTRING('hello', 2, 3) -- 'ell' (2번째부터 3글자)
CONCAT('hello', ' ', 'world')  -- 'hello world'
REPLACE('hello', 'l', 'r')     -- 'herro'
```

---

## 날짜 함수

```sql
NOW()              -- 현재 날짜+시간
CURDATE()          -- 현재 날짜
YEAR(날짜)         -- 연도 추출
MONTH(날짜)        -- 월 추출
DAY(날짜)          -- 일 추출
DATEDIFF(a, b)     -- 날짜 차이 (일수)
DATE_FORMAT(날짜, '%Y-%m-%d')  -- 날짜 포맷
```

---

## 실전 팁

### 실행 순서 기억하기
```
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

### 자주 쓰는 패턴

```sql
-- 상위 N개
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- N번째 값 (LIMIT offset, count)
SELECT * FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;  -- 3번째

-- 그룹별 최댓값 가진 행
SELECT e.*
FROM employees e
INNER JOIN (
    SELECT department, MAX(salary) AS max_sal
    FROM employees GROUP BY department
) m ON e.department = m.department AND e.salary = m.max_sal;
```

### 주의사항

```sql
-- GROUP BY할 때 SELECT에는 GROUP BY 컬럼 or 집계함수만!
SELECT department, name, AVG(salary)  -- ❌ name은 안됨
FROM employees GROUP BY department;

SELECT department, AVG(salary)        -- ✅
FROM employees GROUP BY department;

-- WHERE vs HAVING
WHERE AVG(salary) > 3000   -- ❌ WHERE에 집계함수 불가
HAVING AVG(salary) > 3000  -- ✅
```

---

## 체크리스트

- [ ] 실행 순서 FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- [ ] NULL 비교는 IS NULL / IS NOT NULL
- [ ] GROUP BY 쓰면 SELECT에 집계함수 or GROUP BY 컬럼만
- [ ] 그룹 필터링은 HAVING (집계함수 쓸 수 있음)
- [ ] JOIN 종류 (INNER / LEFT / RIGHT / FULL)
- [ ] COUNT(\*)는 NULL 포함, COUNT(컬럼)은 NULL 제외
