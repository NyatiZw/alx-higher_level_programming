-- A script
-- that creates second_table in database hbtn_0c_0
USE hbtn_0c_0
SET @tble = (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'hbtn_0c_0' table_name = 'second_table');
IF @tble = 0 THEN
	CREATE TABLE second_table (
		id INT,
		name VARCHAR(256),
		score INT
	);
END IF;

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
