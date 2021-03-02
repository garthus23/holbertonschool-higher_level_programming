-- Create user and Grant all privileges
-- Create Users
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all Privileges
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
