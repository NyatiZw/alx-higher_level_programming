-- A Script
-- to compute the score average of all records in the table
SET @dbname := 'hbtn_0c_0';
SET @query := CONCAT(
	'SELECT AVG(score) AS average FROM ', @dbname, '.scond_table;'
);
