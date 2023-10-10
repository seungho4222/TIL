CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId)
      REFERENCES users(id)
);


INSERT INTO
  users (name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


SELECT * FROM articles WHERE id = 1;

-- INNER JOIN
SELECT articles.title, users.name
FROM articles
INNER JOIN users
  ON user.id = articles.userId
WHERE users.id = 1;


-- LEFT JOIN
SELECT *  FROM articles
LEFT JOIN users
  ON users.id = articles.userId;


-- 아티스트별 앨범 수 ??
SELECT count(*) AS AlbumCount, artists.artistid, artists.name AS ArtistName
FROM albums
INNER JOIN artists
  ON albums.artistid = artists.artistid
GROUP BY artists.artistid;

SELECT count(*)
from albums
where artistid = 22;
