-- 테이블 생성
CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);


-- 테이블 스키마(구조) 확인
PRAGMA table_info('examples');


-- 테이블 필드 추가
ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) DEFAULT 'N' NOT NULL;

ALTER TABLE examples
ADD COLUMN Age INTEGER;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100);


-- 테이블 필드명 변경
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;


-- 테이블 필드 삭제
ALTER TABLE examples
DROP COLUMN PostCode;


-- 테이블명 변경
ALTER TABLE examples
RENAME TO new_examples;


-- 테이블 삭제
DROP TABLE examples;





-- 테이블에 데이터 삽입
INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title2', 'content3', '1700-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('mytitle', 'mycontent', DATE());


-- 데이터 변경
UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;


-- 데이터 삭제
DELETE FROM
  articles
WHERE
  id = 1;

DELETE FROM
  articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);