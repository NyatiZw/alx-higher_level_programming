-- A Script
-- to remove all records with score <=5 in second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
