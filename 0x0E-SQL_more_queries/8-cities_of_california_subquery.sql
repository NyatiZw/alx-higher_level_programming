-- A script
-- that lists all specific entries in database

USE hbtn_0d_usa;
SELECT cities, id,
FROM states
WHERE id IS NOT NULL
ORDER BY id ASC;
