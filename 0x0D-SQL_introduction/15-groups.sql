-- A Script
-- to retrieve the score and name colunmns
USE hbtn_0c_0;
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score 
ORDER BY number DESC;
