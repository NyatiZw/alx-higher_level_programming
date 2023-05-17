-- A Script
-- to update the score of Bob without using id value
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'DELETE FROM ', @dbname, '.second_table WHERE score <= 5;'
);

PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
