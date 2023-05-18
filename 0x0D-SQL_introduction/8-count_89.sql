-- A script
-- that displays the number of recods with id=89 in first_table
USE hbtn_0c_0;
SELECT COUNT(*) AS _count
FROM 'first_table'
WHERE id = 89;
