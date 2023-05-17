-- A Script
-- to remove all records with score <=5 in second_table
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'DELETE FROM ', @dbname, '.second_table WHERE score <= 5;'
);

PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
