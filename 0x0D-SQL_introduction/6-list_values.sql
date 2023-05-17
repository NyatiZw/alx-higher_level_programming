-- A script
-- that creates a new table in a database
SET @dbase = 'hbtn_0c_0';
USE @dbase;
SET @tblname = (
	SELECT TABLE_NAME
	FROM INFORMATION_SCHEMA.TABLES
	WHERE TABLE_SCHEMA = @dbase
	LIMIT 1
);

IF @tblname IS NOT NULL THEN
	SET @res = CONCAT('SELECT * FROM ', @dbase, '.', @tblname, ';');

	PREPARE statement FROM @res;
	EXECUTE statement;
	DEALLOCATE PREPARE statement;
END IF;
