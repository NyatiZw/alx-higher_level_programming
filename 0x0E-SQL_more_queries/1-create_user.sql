-- A script
-- that creates the MySQL server user
CREATE USER IF NOT EXITS 'user_0d_1'@'host' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'host' WITH GRANT OPTION;
