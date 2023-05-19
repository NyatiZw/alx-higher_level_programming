-- A script
-- that lists all cities contained in database
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
