-- A script
-- that displays the number of recods with id=89 in first_table
SET @dbase = 'hbtn_0c_0';
USE @dbase;
SELECT COUNT(*) AS _count
FROM 'first_table'
WHERE id = 89;
