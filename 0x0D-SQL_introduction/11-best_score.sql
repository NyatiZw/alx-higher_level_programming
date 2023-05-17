-- A Script
-- to list all records with score >= 10 in second_table
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'SELECT score, name FROM ', @dbname, '.second_table WHERE score >= 10 ORDER BY score DESC;'
);

PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
