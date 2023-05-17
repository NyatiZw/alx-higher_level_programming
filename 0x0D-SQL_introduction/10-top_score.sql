-- A Script
-- to list all records of the table second_table

SET @dbase := 'hbtn_0c_0';
SET @query := CONCAT('SELECT score, name FROM ', @dbase, '.second_table ORDER BY score DESC;'
);
PREPARE statement FROM @query;
EXECUTE statement;
DEALLOCATE PREPARE statement;
