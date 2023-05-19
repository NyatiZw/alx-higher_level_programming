-- A script
-- that lists all cities contained in database

SELECT DISTINCT cities.id, cities.name, states.name
FROM cities, states
ORDER BY ASC;
