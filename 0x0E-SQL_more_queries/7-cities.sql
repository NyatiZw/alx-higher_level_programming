-- A script 
-- that creates database and table
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
USE 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'cities' (
	id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	states_id INT,
	FOREIGN KEY (states_id) REFERENCES states(id)
	);
