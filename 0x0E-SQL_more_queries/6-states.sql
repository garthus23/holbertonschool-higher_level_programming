-- Create Database and Table Default value Uniq auto gen id
-- Create Database and Table Default value Uniq auto gen id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE  hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, name varchar(256) NOT NULL);
