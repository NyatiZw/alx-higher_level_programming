-- A script 
-- that creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	states_id INT NOT NULL FOREIGN KEY,
	FOREIGN KEY (states_id) REFERENCES states,
	name VARCHAR(256) NOT NULL
	);
