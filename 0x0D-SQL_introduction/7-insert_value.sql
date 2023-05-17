-- A script
-- that inserts a new row in the table first_table
SET @dbase = 'hbtn_0c_0';
USE @dbase;
SET @id_val = 89;
SET @name_val = 'Best School';

INSERT INTO 'first_table' (id, name)
VALUES(@id_val, @name_val);
