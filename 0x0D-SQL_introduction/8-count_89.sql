-- A script
-- that inserts a new row in the table first_table
SET @dbase = 'hbtn_0c_0';
USE @dbase;
SELECT COUNT(*) AS _count
FROM 'first_table'
WHERE id = 89
