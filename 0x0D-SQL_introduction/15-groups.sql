-- A Script
-- to compute the score average of all records in the table
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'SELECT score, name FROM ', @dbname, '.second_table WHERE name <> "" ORDER BY score DESC;'
);
