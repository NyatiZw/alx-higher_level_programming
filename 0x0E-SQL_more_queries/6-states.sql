-- A script 
-- that creates database and table
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';

-- Use the database
USE 'hbtn_0d_usa';

-- create a table in the database
CREATE TABLE IF NOT EXISTS 'states' (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
