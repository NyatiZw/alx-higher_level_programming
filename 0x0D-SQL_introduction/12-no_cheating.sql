-- A Script
-- to update the score of Bob without using id value
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'UPDATE ', @dbname, '.second_table SET score = 10 WHERE name = "Bob";'
);

PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
