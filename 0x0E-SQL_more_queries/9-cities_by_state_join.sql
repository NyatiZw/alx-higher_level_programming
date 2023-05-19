-- A script
-- that lists all cities contained in database
USE hbtn_0d_usa;
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities, states
ORDER BY ASC;
