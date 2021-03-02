-- Create Database , Create user and Grant select privileges
-- Create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create Users
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Use hbtn_0d_2
-- Grant all Privileges
GRANT SELECT ON hbtn_0d_2. * TO 'user_0d_2'@'localhost';
