-- A script
-- that prints full description of table
SET @dbase = 'hbtn_0c_0';
SET @tblname = 'first_table';

SET @query = CONCAT('SELECT * FROM information_schema.columns WHERE table_schema = "', @dbase, '" AND table_name = "', @tblname, '";');

PREPARE staatement FROM @query;
EXECUTE statement;
