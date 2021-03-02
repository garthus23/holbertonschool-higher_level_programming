-- Create Database and Table Default value Uniq auto gen id
-- Create Database and Table Default value Uniq auto gen id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE  hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id int NOT NULL,name varchar(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
