-- A Script
-- to remove all records with score <=5 in second_table
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'SELECT score, name FROM ', @dbname, '.second_table WHERE name IS NOT NULL AND name <> "" ORDER BY score DESC;'
);

PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
