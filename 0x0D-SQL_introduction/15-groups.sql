-- A Script
-- to compute the score average of all records in the table
USE hbtn_0c_0;
SELECT score, name FROM second_table WHERE name <> "" ORDER BY score DESC;
