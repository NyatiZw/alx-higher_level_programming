-- A script 
-- that creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	states_id INT NOT NULL
	FOREIGN KEY (states_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	);
