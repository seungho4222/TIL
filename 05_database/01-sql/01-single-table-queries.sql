-- 01. Querying data
SELECT  -- 단일 데이터 조회
  LastName
FROM
  employees;

SELECT  -- 다중 데이터 조희
  LastName, FirstName
FROM
  employees;

SELECT  -- 모든 데이터 조회
  *
FROM
  employees;

SELECT  -- 필드명 지정
  FirstName AS '이름'
FROM
  employees;

SELECT  -- 필드 산술 계산
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;


-- 02. Sorting data
SELECT  -- 오름차순 정렬 (ASC 미입력 동일)
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

SELECT  -- 내림차순 정렬
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT  -- 필드별 정렬
  Country, City
FROM
  customers
ORDER BY  -- 내림차순 정렬된 동일 Counrty 필드 내, City 필드 오름차순 정렬
  Country DESC,
  City ASC;

SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;


-- NULL 정렬 예시
SELECT  -- NULL 값은 가장 먼저 표시
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;


-- 03. Filtering data
SELECT DISTINCT  -- 중복 제거
  Country
FROM
  customers
ORDER BY
  Country;

SELECT
  LastName, FirstName, City
From
  customers
WHERE  -- 조건 문
  City == 'Prague';

SELECT
  LastName, FirstName, City
From
  customers
WHERE  -- 조건문 부정
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE  -- 다중 조건 (AND)
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE  -- 다중 조건 (OR)
  Company IS NULL
  OR Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE  -- 범위 조건 (BETWEEN)
--   Bytes >= 100000
--   AND Bytes <= 500000;
  Bytes BETWEEN 100000 AND 500000;

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY  -- 정렬은 조건문 다음에 위치
  Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE  -- 범위 조건 (IN)
  Country IN ('Canada', 'Germany', 'France');
--   Country = 'Canada'
--   OR Country = 'Germany'
--   OR Country = 'France';

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE  -- 범위 조건 (NOT IN)
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE  -- ~로 끝나는 데이터 조회
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE  -- ~로 끝나는 데이터 조회
  FirstName LIKE '___a';

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;  -- 해당 데이터 개수 출력

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;  -- 건너뛰고, 해당 데이터 개수 출력
-- LIMIT 4 OFFSET 3;


-- 04. Grouping data
SELECT  -- 그룹에 대한 데이터 집계 값 조회
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT  -- 그룹에 대한 데이터 평균 값 조회
  Composer,
  AVG(Bytes) AS avg0fBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avg0fBytes DESC;


-- 에러
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avg0fMinute
FROM
  tracks
WHERE  -- 세부조건 지정 ??
  avg0fMinute < 10
GROUP BY
  Composer;


-- 에러 해결
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avg0fMinute
FROM
  tracks
GROUP BY
  Composer
HAVING  -- 집계항목에 대한 세부 조건 지정
  avg0fMinute < 10;
